from database import database
from models.hotel_model import HotelModel


class HotelRepository:
    @classmethod
    def get_all(cls):
        return HotelModel.query.all()

    @classmethod
    def get_by_id(cls, hotel_id):
        hotel = HotelModel.query.filter_by(id=hotel_id).first()
        if hotel:
            return hotel
        return None

    @classmethod
    def add(cls, new_hotel):
        database.session.add(new_hotel)
        database.session.commit()

    @classmethod
    def delete(cls, hotel):
        database.session.delete(hotel)
        database.session.commit()
