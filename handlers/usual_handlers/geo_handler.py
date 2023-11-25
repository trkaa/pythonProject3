from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot, F
from keyboards import navikeyboard
from functions import point_time, rite_user_state, get_distance


db = DataBase()
geo_router = Router()


@geo_router.message(F.photo)
async def catch_photo(message: Message):
    print(message.photo[-1].file_id)


@geo_router.message(F.location)
async def get_geo(message: Message, bot: Bot):
    s = int(db.load_state(message.from_user.id)[0])

    if s == 0:

        point_1 = {"latitude": 55.107270, "longitude": 38.763697}
        distance = get_distance(point_1, message)

        if distance < float(100000.0):

            current_state = str(1)
            rite_user_state(current_state, message)
            point_time('point1', message)
            id_picture = int(2)
            picture = db.get_picture(id_picture)[0]
            id_text = int(2)
            text = db.get_text(id_text)[0]
            scene1_pic_list = [2, 3, 2, 3, 2, 3, 2]
            scene1_text_list = [2, 3, 4, 5, 6, 7, 8]
            cur_id = 1
            scene_id = 1
            # await bot.send_photo(message.from_user.id, photo=picture, caption=text,
            #                      )
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene1_pic_list, scene1_text_list, cur_id, scene_id))

        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')
