from flask import Flask
from flask_restful import Api
from resources.hotel_resources import Hotel, Hotels
from resources.user_resources import UserRegistration, UserLogin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///HotelsApi.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')

api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == "__main__":
    from database import database

    database.init_app(app)
    with app.app_context():
        database.create_all()
    app.run(debug=True)
