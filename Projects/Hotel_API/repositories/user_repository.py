from database import database
from models.user_model import UserModel


class UserRepository:
    @classmethod
    def get_by_username(cls, username):
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return user
        return None

    @classmethod
    def get_by_public_id(cls, public_id):
        user = UserModel.query.filter_by(public_id=public_id).first()
        if user:
            return user
        return None

    @classmethod
    def add(cls, new_user):
        database.session.add(new_user)
        database.session.commit()

