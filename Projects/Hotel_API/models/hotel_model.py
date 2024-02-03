from database import database


class HotelModel(database.Model):
    __tablename__ = "Hotel"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    rating = database.Column(database.Float(precision=1))
    value = database.Column(database.Float(precision=2))
    city = database.Column(database.String(80))

    def __init__(self, _id, name, rating, value, city):
        self.id = _id
        self.name = name
        self.rating = rating
        self.value = value
        self.city = city
