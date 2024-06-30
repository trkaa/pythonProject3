import sqlite3


class DataBase:
    db_path = 'database/16century_quest.db'

    @staticmethod
    def execute(sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = sqlite3.connect(DataBase.db_path)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict, _and: bool = True) -> tuple:
        sql += (' AND ' if _and else ', ').join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def create_table_check_points(self):
        sql = '''CREATE TABLE IF NOT EXISTS check_points (id_player INTEGER PRIMARY KEY AUTOINCREMENT ,telegram_id 
        INTEGER , name VARCHAR, intro_checkpoint VARCHAR, point1 VARCHAR, point2 VARCHAR, point3 VARCHAR, 
        point4 VARCHAR, point5 VARCHAR, point6 VARCHAR, point7 VARCHAR, point8 VARCHAR, point9 VARCHAR, 
        point10 VARCHAR, point11 VARCHAR, point12 VARCHAR, point13 VARCHAR, point14 VARCHAR, point15 VARCHAR, 
        point16 VARCHAR, point17 VARCHAR, point18 VARCHAR, point19 VARCHAR, point20 VARCHAR, user_state VARCHAR, 
        sell_price VARCHAR, seller VARCHAR, pay_time VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_text(self):
        sql = '''CREATE TABLE IF NOT EXISTS quest_text (id_text INTEGER PRIMARY KEY ,text VARCHAR, text_capture 
        VARCHAR)'''
        self.execute(sql, commit=True)

    def create_table_pictures(self):
        sql = '''CREATE TABLE IF NOT EXISTS pictures (id_picture INTEGER PRIMARY KEY ,picture_fileid VARCHAR, 
        pic_capture VARCHAR)'''
        self.execute(sql, commit=True)

    def new_user(self, user_tuple: tuple):
        sql = '''INSERT INTO check_points (telegram_id, name) VALUES (?, ?)'''
        self.execute(sql, user_tuple, commit=True)

    def user_exist(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT name FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

    def get_users(self):
        sql = '''SELECT telegram_id FROM check_points'''
        return self.execute(sql, fetchall=True)

    def point_time(self, point: str, user_time: tuple):
        sql = f'''UPDATE check_points SET {point}=? WHERE telegram_id=? '''
        self.execute(sql, user_time, commit=True)

    def user_state(self, current_state: tuple):
        sql = '''UPDATE check_points SET user_state=? WHERE telegram_id=? '''
        self.execute(sql, current_state, commit=True)

    def load_state(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT user_state FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

    def get_picture(self, id_picture: int):
        parameters = (id_picture,)
        sql = '''SELECT picture_fileid FROM pictures WHERE id_picture=?'''
        return self.execute(sql, parameters, fetchone=True)

    def get_text(self, id_text: int):
        parameters = (id_text,)
        sql = '''SELECT text FROM quest_text WHERE id_text=?'''
        return self.execute(sql, parameters, fetchone=True)

    def write_promo(self, seller_promo_code: str):
        parameters = (seller_promo_code,)
        sql = '''INSERT INTO promo_code (code) VALUES (?)'''
        self.execute(sql, parameters, commit=True)

    def load_code(self):
        # parameters = (user_id,)
        sql = '''SELECT * FROM promo_code'''
        return self.execute(sql, fetchall=True)

    def clear_code(self, id_code: int):
        parameters = (id_code,)
        sql = '''DELETE FROM promo_code WHERE id=?'''
        self.execute(sql, parameters, commit=True)

    def write_sell_price(self, user_price: tuple):
        sql = '''UPDATE check_points SET sell_price=? WHERE telegram_id=? '''
        self.execute(sql, user_price, commit=True)

    def write_seller(self, user_seller: tuple):
        sql = '''UPDATE check_points SET seller=? WHERE telegram_id=? '''
        self.execute(sql, user_seller, commit=True)

    def write_sell_price_seller(self, user_price_seller: tuple):
        sql = '''UPDATE check_points SET sell_price=?, seller=? WHERE telegram_id=?  '''
        self.execute(sql, user_price_seller, commit=True)

    def load_price(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT sell_price FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

    def load_seller(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT seller FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

    def pay_time(self, user_time: tuple):
        sql = f'''UPDATE check_points SET pay_time=? WHERE telegram_id=? '''
        self.execute(sql, user_time, commit=True)

    def seller_table_insert(self, seller_table: str, seller_tuple: tuple):
        sql = f'''INSERT INTO {seller_table} (telegram_id, name, sell_time, price) VALUES (?, ?, ?, ?)'''
        self.execute(sql, seller_tuple, commit=True)



