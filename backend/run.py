from flask_jwt_extended import JWTManager

from app import app
from route import api


app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(
        port=5005,
        host='0.0.0.0',
        debug=True
    )
