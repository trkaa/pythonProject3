from aiogram import Bot, Router, F
from aiogram.types import Message
from database import DataBase
from keyboards import geo_kb, ikb_promo_input_start_ikb, ikb_first_point
from geo_points import point_1
from functions import rite_user_state, point_time

first_place_router = Router()
second_buy_router = Router()
db = DataBase()


@first_place_router.callback_query(F.data == 'first_point')
async def show_first_point(message: Message, bot: Bot):
    s = int(db.load_state(message.from_user.id)[0])
    if s == 0:
        await bot.send_location(message.from_user.id, latitude=point_1['latitude'], longitude=point_1['longitude'],
                                reply_markup=geo_kb())
    else:
        pass


@second_buy_router.callback_query(F.data == 'input_pay')
async def second_buy_promo(message: Message, bot: Bot):
    current_state = str(0)
    rite_user_state(current_state, message)
    point_time('intro_checkpoint', message)
    id_picture = int(1)
    picture = db.get_picture(id_picture)[0]
    id_text = int(1)
    text = db.get_text(id_text)[0]
    await bot.send_photo(message.from_user.id, photo=picture, caption=text)
    await bot.send_message(message.from_user.id, text=db.get_text(20)[0], reply_markup=ikb_first_point())



