from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.time_card import TimeCardModel


class TimeCard(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'enter',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'out',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'user_id',
        type=int,
        required=True,
        help="This field cannot be blank."
    )

    @jwt_required()
    def get(self, id):
        time_card = TimeCardModel.find_by_id(id)
        if time_card:
            return time_card.json()
        return {'message': 'Time card not found'}, 404

    @jwt_required()
    def post(self):
        message = {"message": "A time card with that enter already exists"}
        data = TimeCard.parser.parse_args()

        if TimeCardModel.find_by_enter(data['enter']):
            return message, 400

        time_card = TimeCardModel(data['enter'], data['out'], data['user_id'])
        time_card.save_to_db()

        return {"message": "Time card created successfully."}, 201
