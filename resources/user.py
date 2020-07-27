import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help='This field cannot be empty'
    )
    parser.add_argument('password',
            type=str,
            required=True,
            help='This field cannot be empty'
    )

    def post(self):
        request_data=UserRegister.parser.parse_args()

        if UserModel.find_by_username(request_data['username']):
            return {'message':'A user with the username already exists'}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'insert into users values (NULL, ?, ?)'
        # cursor.execute(query, (request_data['username'], request_data['password']))

        # connection.commit()
        # connection.close()

        # user = UserModel(request_data['username'], request_data['password'])
        user = UserModel(**request_data)
        user.save_to_db()

        return {'message':'User created successfully'}, 201