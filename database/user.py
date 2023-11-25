from aiogram.types import Message

from database.base import DataBase


class User(DataBase):

    def __init__(self, data: tuple | Message):
        super().__init__()
        user_id = data.from_user.id if isinstance(data, Message) else int(data[0])
        if not self.read(user_id=user_id):
            User.create(data)
        self.user_id = data[0]
        self.name = data[1]
        self.phone = data[2]
        self.address = data[3]
        self.status = data[4]
        self.is_admin = data[5]

    @staticmethod
    def create_table():
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (user_id INTEGER PRIMARY KEY, name VARCHAR, phone VARCHAR,
        address VARCHAR, status INTEGER, is_admin INTEGER)'''
        DataBase.execute(sql, commit=True)

    @staticmethod
    def create(data: tuple):
        sql = 'INSERT INTO users (user_id, name, phone, address, status, is_admin) VALUES (?, ?, ?, ?, ?, ?)'
        DataBase.execute(sql, data, commit=True)

    @staticmethod
    def is_exists(user_id: int):
        sql = 'SELECT * FROM users WHERE user_id=?'
        return DataBase.execute(sql, (user_id,), fetchone=True)

    @staticmethod
    def is_admin(user_id: int) -> bool:
        sql = 'SELECT is_admin FROM users WHERE user_id=?'
        user = DataBase.execute(sql, (user_id,), fetchone=True)
        return bool(user[0]) if user else False

    def read(self, **kwargs):
        sql = '''SELECT * FROM users WHERE '''
        sql, params = DataBase.extract_kwargs(sql, kwargs)
        return DataBase.execute(sql, params, fetchone=True)

    def update(self, **kwargs):
        sql = '''UPDATE users SET '''
        sql, params = DataBase.extract_kwargs(sql, kwargs, _and=False)
        sql = sql + f' WHERE user_id={self.user_id}'
        self.execute(sql, params, commit=True)

    def delete(self):
        sql = f'DELETE FROM users WHERE user_id={self.user_id}'
        del self
        return DataBase.execute(sql, commit=True)

    def __str__(self):
        return str([*self.__dict__.values()])