from db import db


class AuthModel(db.Model):
    __tablename__ = 'authorization'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120))
    scope = db.Column(db.String(40))

    def __init__(self, code, scope):
        self.code = code
        self.scope = scope

    def json(self):
        return {'code': self.code, 'scope': self.scope}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

