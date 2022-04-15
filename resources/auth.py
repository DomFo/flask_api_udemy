from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import render_template

from models.item import ItemModel


class Auth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('state',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('code',
                        type=str,
                        required=True,
                        help="Every item needs a store id")
    parser.add_argument('scope',
                        type=str,
                        required=True,
                        help="Every item needs a store id")

    def get(self):
        data = Auth.parser.parse_args()
        print(data)
        return render_template('hello.html')

