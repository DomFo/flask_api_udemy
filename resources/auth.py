from flask_restful import Resource, reqparse
from flask import make_response, render_template
import requests
from constants import *

from models.subject import SubjectModel


class Auth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('code', type=str, location='args')
    parser.add_argument('scope', type=str, location='args')

    def get(self):
        data = Auth.parser.parse_args()
        print(data)
        if data['code']:
            data = self.get_tokens(code=data['code'])
            subject = SubjectModel(data)
            if not SubjectModel.find_by_strava_id(subject['strava_id']):
                subject.save_to_db()
        return make_response(render_template('hello.html'), 200)

    def get_tokens(self, code):
        # Make Strava auth API call with client_id, client_secret and code
        response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'code': code,
                'grant_type': 'authorization_code'
            }
        )
        if response.status_code == 200:
            return response.json()

