from db import db
import requests
from constants import *


class SubjectModel(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    strava_id = db.Column(db.Integer)
    sex = db.Column(db.String(2))
    access_token = db.Column(db.String(80))
    refresh_token = db.Column(db.String(80))

    def __init__(self, data):
        self.strava_id = data['athlete']['id']
        self.sex = data['athlete']['sex']
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']

    def json(self):
        return {
            'id': self.id,
            'strava_id': self.strava_id,
            'sex': self.sex,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_new_tokens(self):
        # Make Strava auth API call with client_id, client_secret and code
        response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'code': self.refresh_token,
                'grant_type': 'refresh_token'
            }
        )
        data = response.json()
        return data['access_token'], data['refresh_token']

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_strava_id(cls, strava_id):
        return cls.query.filter_by(strava_id=strava_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

