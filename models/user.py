import sqlite3

from db import db

class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod # because we are returning a class object
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'select * from users where username=?'
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()

        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # user = cls(row[0], row[1], row[2]) # because class method
        #     user = cls(*row) # as the parameters match with the result set columns, we can pass varargs as *row
        # else:
        #     user = None
        
        # connection.close()
        # return user

        return cls.query.filter_by(username=username).first()

    @classmethod # because we are returning a class object
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'select * from users where id=?'
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()

        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # user = cls(row[0], row[1], row[2]) # because class method
        #     user = cls(*row) # as the parameters match with the result set columns, we can pass varargs as *row
        # else:
        #     user = None
        
        # connection.close()
        # return user

        return cls.query.filter_by(id=_id).first()