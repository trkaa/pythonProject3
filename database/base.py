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
        point16 VARCHAR, point17 VARCHAR, point18 VARCHAR, point19 VARCHAR, point20 VARCHAR, user_state VARCHAR)'''
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
