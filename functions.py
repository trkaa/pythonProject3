from decimal import Decimal
from datetime import datetime
from geopy.distance import geodesic
from aiogram.types import Message
from database import DataBase

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
