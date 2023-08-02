from datetime import timedelta

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    # jwt_refresh_token_required,
    get_jwt_identity,
    # get_raw_jwt
)

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

    def get(self):
        return {
            'message': 'Hello, World!'
        }


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
