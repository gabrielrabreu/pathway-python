import jwt
from functools import wraps
from flask import request

from app_config import SECRET_KEY
from repositories.user_repository import UserRepository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return {'message': 'Token is missing!'}, 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = UserRepository().get_by_public_id(data['public_id'])
        except Exception as ex:
            print(ex)
            return {'message': 'Token is invalid!'}, 401

        return f(current_user, *args, **kwargs)

    return decorated
