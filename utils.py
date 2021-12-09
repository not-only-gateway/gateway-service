import jwt
import requests
from simplejson import JSONDecodeError
import env
from datetime import datetime, timedelta
import sys
from sqlalchemy.exc import SQLAlchemyError


def make_jwt(package):
    return jwt.encode(
        package,
        env.SECURE_TOKEN,
        algorithm='HS256'
    )


def decrypt_jwt(token):
    try:
        token = jwt.decode(
            token,
            key=env.SECURE_TOKEN,
            algorithms='HS256'
        )

        return token
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidTokenError, jwt.exceptions.ExpiredSignatureError):
        return None
