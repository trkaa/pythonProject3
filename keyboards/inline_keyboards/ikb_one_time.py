from aiogram.utils.keyboard import InlineKeyboardBuilder


def ikb_first_point():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='как пройти к башне', callback_data='first_point')
    return keyboard.as_markup(resize_keyboard=True)
