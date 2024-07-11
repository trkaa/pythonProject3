from aiogram.utils.keyboard import KeyboardBuilder
from aiogram.types import KeyboardButton


def geo_kb():
    keyboard = KeyboardBuilder(KeyboardButton)
    loca_but = KeyboardButton(text='Я НА МЕСТЕ', request_location=True)
    keyboard.add(loca_but)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)
