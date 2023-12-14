from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot
from aiogram.filters import Command
from keyboards import geo_kb, ikb_first_point
from functions import point_time, rite_user_state

db = DataBase()
start_router = Router()


@start_router.message(Command('start'))
async def mes_start(message: Message, bot: Bot):
    # print(message)
    user_id = message.from_user.id
    user_tuple = (message.from_user.id, message.from_user.full_name)
    if db.user_exist(user_id) is None:
        db.new_user(user_tuple)
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
        await bot.send_message(message.from_user.id,  text=db.get_text(20)[0], reply_markup=ikb_first_point())
        # await bot.send_location(message.from_user.id, latitude=55.107270, longitude=38.763697, reply_markup=geo_kb())
    else:
        pass



