# import sqlite3

from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name=name
        self.price=price
        self.store_id=store_id
    
    def json(self):
        return {'name':self.name, 'price':self.price, 'store_id':self.store_id}

    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = 'select * from items where name=?'

        # result = cursor.execute(query, (name,))
        # row = result.fetchone()

        # connection.close()

        # if row:
        #     return cls(*row)
        return cls.query.filter_by(name=name).first()
    
    # below method takes care of both insert and update to the DB with the values
    # hence we can use the same method in both the places
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def insert(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = 'insert into items values (?, ?)'

    #     result = cursor.execute(query, (self.name, self.price))

    #     connection.commit()
    #     connection.close()
        

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = 'update items set price=? where name=?'

    #     result = cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()