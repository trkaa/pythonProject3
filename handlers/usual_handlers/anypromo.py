from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot
from aiogram.filters import Command
from keyboards import geo_kb, ikb_first_point
from functions import get_code
import os

master_id = os.getenv('MASTER_ID')
db = DataBase()
anypromo_router = Router()


@anypromo_router.message(Command('anypromo'))
async def get_anypromo(message: Message, bot: Bot):
    seller_name = str('any')
    seller_promo_code = str(seller_name + get_code())
    # print(seller_promo_code)
    # print(seller_promo_code[:-6])
    db.write_promo(seller_promo_code)


@anypromo_router.message(Command('freepromo'))
async def get_freepromo(message: Message, bot: Bot):
    user_id = message.from_user.id
    if int(master_id) == int(user_id):
        seller_name = str('free')
        seller_promo_code = str(seller_name + get_code())
        db.write_promo(seller_promo_code)
        await bot.send_message(message.from_user.id, text=seller_promo_code)
    else:
        pass


@anypromo_router.message(Command('ligapromo'))
async def get_freepromo(message: Message, bot: Bot):
    user_id = message.from_user.id
    if int(5224860941) == int(user_id):
        seller_name = str('liga')
        seller_promo_code = str(seller_name + get_code())
        db.write_promo(seller_promo_code)
        await bot.send_message(message.from_user.id, text=seller_promo_code)
    else:
        pass
