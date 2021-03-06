from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

# import sqlite3

from models.item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be empty'
        )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help='Store id cannot be empty'
        )
    
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {'message':'Item not found'}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message':f'An item with the name {name} already exist'}, 400

        request_data=self.parser.parse_args()
        item = ItemModel(name, request_data['price'], request_data['store_id'])
        
        try:
            # item.insert()
            item.save_to_db()
        except:
            return {'message':'An error occurred inserting the item'}, 500
        return item.json(), 201
        
    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = 'delete from items where name=?'

        # result = cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'Item deleted'}, 200

    def put(self, name):
        request_data = self.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, request_data['price'])

        # if item:
        #     try:
        #         updated_item.update()
        #     except:
        #         return {'message':'An error occurred inserting the item'}, 500
        # else:
        #     try:
        #         updated_item.insert()
        #     except:
        #         return {'message':'An error occurred inserting the item'}, 500
        # return updated_item.json(), 201

        if item:
            item.price = request_data['price']
            
        else:
            item = ItemModel(name, request_data['price'], request_data['store_id'])
        item.save_to_db()
        return item.json(), 201


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = 'select * from items'

        # result = cursor.execute(query)

        # items=[]
        # for row in result:
        #     items.append({'name':row[0], 'price':row[1]})
        
        # connection.close()

        # return {'items':items}

        return {'items':[item.json() for item in ItemModel.query.all()]}
        # return {'items':list(map(lambda x: x.json(), ItemModel.query.all()))}