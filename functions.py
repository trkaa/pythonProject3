from decimal import Decimal
from datetime import datetime
from geopy.distance import geodesic
from aiogram.types import Message
from database import DataBase
import random

db = DataBase()


def get_distance(gpoint: dict, message: Message):
    latitude1 = Decimal(message.location.latitude)
    latitude1 = latitude1.quantize(Decimal('1.000000'))
    longitude1 = Decimal(message.location.longitude)
    longitude1 = longitude1.quantize(Decimal('1.000000'))
    latitude2 = Decimal(gpoint['latitude'])
    latitude2 = latitude2.quantize(Decimal('1.000000'))
    longitude2 = Decimal(gpoint['longitude'])
    longitude2 = longitude2.quantize(Decimal('1.000000'))
    point_1_tuple = (latitude1, longitude1)
    user_point_tuple = (latitude2, longitude2)
    distance = geodesic(point_1_tuple, user_point_tuple).m
    return distance


def point_time(point: str, message: Message):
    time = str(datetime.now())
    user_id = message.from_user.id
    user_time = (time, user_id)
    point = str(point)
    db.point_time(point, user_time)


def rite_user_state(current_state: str, message: Message):
    user_id = message.from_user.id
    current_state = (current_state, user_id)
    db.user_state(current_state)


def pay_time(message: Message):
    time = str(datetime.now())
    user_id = message.from_user.id
    user_time = (time, user_id)
    db.pay_time(user_time)


def get_code():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    # Соединяем все строки в одну
    str4 = str1 + str2
    # Преобразуем получившуюся строку в список
    ls = list(str4)
    # Тщательно перемешиваем список
    random.shuffle(ls)
    # Извлекаем из списка 6 произвольных значений
    psw = ''.join([random.choice(ls) for x in range(6)])
    # Пароль готов
    # print(psw)
    # Выведет: '1t9G4YPsQ5L7'
    return str(psw)


def insert_seller_table(message: Message):
    time = str(datetime.now())
    telegram_id = message.from_user.id
    name = message.from_user.full_name
    load_seller = str(db.load_seller(telegram_id)[0])
    price = db.load_price(telegram_id)[0]
    # print(price)
    # print(load_seller)

    if load_seller == 'any':
        seller_table = 'any_sell'
        seller_tuple = (telegram_id, name, time, price)
        # print(seller_tuple)
        # print(seller_table)
        db.seller_table_insert(seller_table, seller_tuple)
    if load_seller == 'base':
        seller_table = 'base'
        seller_tuple = (telegram_id, name, time, price)
        # print(seller_tuple)
        # print(seller_table)
        db.seller_table_insert(seller_table, seller_tuple)
    if load_seller == 'free':
        seller_table = 'free'
        seller_tuple = (telegram_id, name, time, price)
        # print(seller_tuple)
        # print(seller_table)
        db.seller_table_insert(seller_table, seller_tuple)
    if load_seller == 'liga':
        seller_table = 'liga'
        seller_tuple = (telegram_id, name, time, price)
        db.seller_table_insert(seller_table, seller_tuple)
