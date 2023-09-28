from datetime import timedelta
from typing import Final
import json

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
)
from flask import jsonify

from logger import logger


parser = reqparse.RequestParser()
parser.add_argument(
    'username',
    help='This field cannot be blank',
    required=True
)
parser.add_argument(
    'password',
    help='This field cannot be blank',
    required=True
)


class Demo(Resource):
    DATA_PATH: Final = './data/data.json'

    def get(self):
        try:
            with open(self.DATA_PATH, 'r') as json_file:
                data = json.load(json_file)
        except Exception:
            return jsonify({
                'message': 'Data not Found!'
            })
        else:
            return jsonify(data)


class UserRegistration(Resource):

    def post(self):
        data = parser.parse_args()
        logger.info(f'UserRegistration > post > data > {data}')

        username = data['username']
        # password = data['password']

        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(hours=24)
        )
        refresh_token = create_refresh_token(identity=username)
        logger.info(f'UserRegistration > post > access_token > {access_token}')
        logger.info(f'UserRegistration > post > refresh_token > {refresh_token}')

        return {
            'message': 'User {} was created'.format(data['username']),
            'access_token': access_token,
            'refresh_token': refresh_token
        }


class SecretResource(Resource):

    @jwt_required()
    def get(self):
        return {
            'answer': 42
        }
