from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import render_template

from models.item import ItemModel


class Auth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('state', type=str, location='args')
    parser.add_argument('code', type=str, location='args')
    parser.add_argument('scope', type=str, location='args')

    def get(self):
        data = Auth.parser.parse_args()
        print(data)
        if data['code']:
            return render_template('hello.html')
        else:
            return render_template('hello.html')

