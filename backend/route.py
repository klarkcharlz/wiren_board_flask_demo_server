from flask_restful import Api

from app import app
from resources import (
    Demo,
    UserRegistration,
    SecretResource
)

api = Api(app)

api.add_resource(
    Demo,
    '/',
)

api.add_resource(
    UserRegistration,
    '/register',
)

api.add_resource(
    SecretResource,
    '/secret',
)
