from database import database


class UserModel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    public_id = database.Column(database.String(50), unique=True)
    username = database.Column(database.String(50), unique=True)
    password = database.Column(database.String(80))

    def __init__(self, public_id, username, password):
        self.public_id = public_id
        self.username = username
        self.password = password
