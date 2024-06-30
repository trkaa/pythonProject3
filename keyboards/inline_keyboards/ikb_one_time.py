from aiogram.utils.keyboard import InlineKeyboardBuilder


def ikb_first_point():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='как пройти к башне?', callback_data='first_point')
    return keyboard.as_markup(resize_keyboard=True)


def ikb_promo_input_start_ikb():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='ввести промокод', callback_data='payments')
    keyboard.button(text='оплатить без промокода', callback_data='final_sale')
    return keyboard.as_markup(resize_keyboard=True)


def ikb_final_sale():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='перейти к оплате', callback_data='final_sale')
    return keyboard.as_markup(resize_keyboard=True)


def cansel_fsm():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='оплатить без промокода', callback_data='final_sale')
    keyboard.button(text='назад', callback_data='cansel_fsm')
    return keyboard.as_markup(resize_keyboard=True)


def ikb_second_buy():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='нет', callback_data='up')
    keyboard.button(text='да', callback_data='final_sale')
    return keyboard.as_markup(resize_keyboard=True)


def ikb_second_buy_promo():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='нет', callback_data='up')
    keyboard.button(text='да', callback_data='input_pay')
    return keyboard.as_markup(resize_keyboard=True)
