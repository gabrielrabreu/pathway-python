from flask_restful import Resource, reqparse, fields, marshal_with

from decorators.token_required import token_required
from models.hotel_model import HotelModel
from repositories.hotel_repository import HotelRepository

hotel_post_args = reqparse.RequestParser()
hotel_post_args.add_argument("name", type=str, help="Name of the hotel is required", required=True)
hotel_post_args.add_argument("rating", type=float, help="Rating of the hotel is required", required=True)
hotel_post_args.add_argument("value", type=float, help="Value of the hotel is required", required=True)
hotel_post_args.add_argument("city", type=str, help="City of the hotel is required", required=True)

hotel_put_args = reqparse.RequestParser()
hotel_put_args.add_argument("name", type=str, help="Name of the hotel is required")
hotel_put_args.add_argument("rating", type=float, help="Rating of the hotel is required")
hotel_put_args.add_argument("value", type=float, help="Value of the hotel is required")
hotel_put_args.add_argument("city", type=str, help="City of the hotel is required")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'rating': fields.Float,
    'value': fields.Float,
    'city': fields.String
}


class Hotels(Resource):
    @token_required
    @marshal_with(resource_fields)
    def get(self, current_user):
        hotels = HotelRepository().get_all()
        return hotels


class Hotel(Resource):
    @token_required
    @marshal_with(resource_fields)
    def get(self, current_user, hotel_id):
        hotel = HotelRepository().get_by_id(hotel_id)
        if not hotel:
            return {'message': 'Hotel not found'}, 404
        return hotel

    @token_required
    @marshal_with(resource_fields)
    def post(self, current_user, hotel_id):
        if HotelRepository().get_by_id(hotel_id):
            return {'message': 'Hotel already exists'}, 400
        args = hotel_post_args.parse_args()
        new_hotel = HotelModel(hotel_id, args['name'], args['rating'], args['value'], args['city'])
        HotelRepository().add(new_hotel)
        return new_hotel, 200

    @token_required
    @marshal_with(resource_fields)
    def put(self, current_user, hotel_id):
        args = hotel_put_args.parse_args()
        hotel = HotelRepository().get_by_id(hotel_id)
        if not hotel:
            return {'message': 'Hotel not found'}, 404
        if args['name']:
            hotel.name = args['name']
        if args['rating']:
            hotel.rating = args['rating']
        if args['value']:
            hotel.value = args['value']
        if args['city']:
            hotel.city = args['city']
        return hotel, 200

    @token_required
    def delete(self, current_user, hotel_id):
        hotel = HotelRepository().get_by_id(hotel_id)
        if not hotel:
            return {'message': 'Hotel not found'}, 404
        HotelRepository().delete(hotel)
        return '', 204
