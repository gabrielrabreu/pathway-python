import uuid
import jwt
import datetime

from flask import make_response, request
from flask_restful import Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash

from app_config import SECRET_KEY
from models.user_model import UserModel
from repositories.user_repository import UserRepository

user_resource_fields = {
    'public_id': fields.String,
    'username': fields.String
}


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'])
        new_user = UserModel(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password)
        UserRepository().add(new_user)
        return {'message': 'User created successfully'}, 200


class UserLogin(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required!"'})

        user = UserRepository().get_by_username(auth.username)

        if not user:
            return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required!"'})

        if check_password_hash(user.password, auth.password):
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                SECRET_KEY)
            return {'token': token}, 200

        return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required!"'})
