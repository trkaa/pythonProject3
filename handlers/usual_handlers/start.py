from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandStart
from keyboards import ikb_promo_input_start_ikb, ikb_final_sale, ikb_second_buy, ikb_second_buy_promo, ikb_first_point
import os
from functions import rite_user_state, point_time

db = DataBase()
start_router = Router()
base_price = os.getenv('BASE_PRICE')


@start_router.message(CommandStart(deep_link=True, magic=F.args == 'any'))
async def mes_start_deep_link(message: Message, bot: Bot):
    # print(message)
    user_id = message.from_user.id
    user_tuple = (message.from_user.id, message.from_user.full_name)
    if db.user_exist(user_id) is None:
        db.new_user(user_tuple)
    state = db.load_state(message.from_user.id)[0]

    coef = 10
    price = int(int(base_price) * (100 - coef) / 100)
    seller = 'any'
    user_price_seller = (price, seller, message.from_user.id)
    db.write_sell_price_seller(user_price_seller)
    if state is None:
        current_state = str(0)
        rite_user_state(current_state, message)
        point_time('intro_checkpoint', message)
        id_picture = int(1)
        picture = db.get_picture(id_picture)[0]
        id_text = int(1)
        text = db.get_text(id_text)[0]
        await bot.send_photo(message.from_user.id, photo=picture, caption=text)
        await bot.send_message(message.from_user.id, text=db.get_text(20)[0], reply_markup=ikb_first_point())

    #     id_picture = int(113)
    #     picture = db.get_picture(id_picture)[0]
    #     await bot.send_photo(message.from_user.id, photo=picture, reply_markup=ikb_final_sale())
    # else:
    #
    #     await bot.send_message(message.from_user.id, text='Вы хотите начать квест заново? \n (потребуется '
    #                                                       'новая оплата)', reply_markup=ikb_second_buy())
        # pass


@start_router.message(Command('start'))
async def mes_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_tuple = (message.from_user.id, message.from_user.full_name)
    coef = 0
    price = int(int(base_price) * (100 - coef) / 100)
    seller = 'base'
    user_price_seller = (price, seller, message.from_user.id)
    db.write_sell_price_seller(user_price_seller)
    if db.user_exist(user_id) is None:
        db.new_user(user_tuple)
        coef = 0
        price = int(int(base_price) * (100 - coef) / 100)
        seller = 'base'
        user_price_seller = (price, seller, message.from_user.id)
        db.write_sell_price_seller(user_price_seller)
    state = db.load_state(message.from_user.id)[0]
    if state is None:
        current_state = str(0)
        rite_user_state(current_state, message)
        point_time('intro_checkpoint', message)
        id_picture = int(1)
        picture = db.get_picture(id_picture)[0]
        id_text = int(1)
        text = db.get_text(id_text)[0]
        await bot.send_photo(message.from_user.id, photo=picture, caption=text)
        await bot.send_message(message.from_user.id, text=db.get_text(20)[0], reply_markup=ikb_first_point())
    #     id_picture = int(113)
    #     picture = db.get_picture(id_picture)[0]
    #     await bot.send_photo(message.from_user.id, photo=picture, reply_markup=ikb_promo_input_start_ikb())
    # else:
    #     await bot.send_message(message.from_user.id, text='Вы хотите начать квест заново? \n (потребуется '
    #                                                       'новая оплата)', reply_markup=ikb_second_buy_promo())



# @start_router.message(Command('start'))
# async def mes_start(message: Message, bot: Bot):
#     # print(message)
#     user_id = message.from_user.id
#     user_tuple = (message.from_user.id, message.from_user.full_name)
#     if db.user_exist(user_id) is None:
#         db.new_user(user_tuple)
#     state = db.load_state(message.from_user.id)[0]
#     if state is None:
#         current_state = str(0)
#         rite_user_state(current_state, message)
#         point_time('intro_checkpoint', message)
#         id_picture = int(1)
#         picture = db.get_picture(id_picture)[0]
#         id_text = int(1)
#         text = db.get_text(id_text)[0]
#         await bot.send_photo(message.from_user.id, photo=picture, caption=text)
#         await bot.send_message(message.from_user.id,  text=db.get_text(20)[0], reply_markup=ikb_first_point())
#         # await bot.send_location(message.from_user.id, latitude=55.107270, longitude=38.763697, reply_markup=geo_kb())
#     else:
#         pass
