from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot, F
from keyboards import navikeyboard
from functions import point_time, rite_user_state, get_distance
from lists import scene1_pic_list, scene1_text_list, scene2_pic_list, scene2_text_list, scene3_pic_list,\
    scene3_text_list, scene4_text_list, scene4_pic_list, scene5_text_list, scene5_pic_list, scene6_text_list,\
    scene6_pic_list, scene7_text_list, scene7_pic_list, scene8_text_list, scene8_pic_list, scene9_text_list,\
    scene9_pic_list, scene10_text_list, scene10_pic_list, scene11_pic_list, scene11_text_list, scene12_pic_list,\
    scene12_text_list, scene13_pic_list, scene13_text_list, scene14_pic_list, scene14_text_list, scene15_pic_list,\
    scene15_text_list, scene16_text_list, scene16_pic_list, scene17_pic_list, scene17_text_list, scene18_pic_list,\
    scene18_text_list, scene19_pic_list, scene19_text_list, scene20_pic_list, scene20_text_list
from geo_points import point_1, point_2, point_3, point_4, point_5, point_6, point_7, point_8, point_9, point_10,\
    point_11, point_12, point_13, point_14, point_15, point_16, point_17, point_18, point_19, point_20

db = DataBase()
geo_router = Router()


@geo_router.message(F.photo)
async def catch_photo(message: Message):
    print(message.photo[-1].file_id)


@geo_router.message(F.audio)
async def catch_audio(message: Message):
    print(message.audio)


@geo_router.message(F.location)
async def get_geo(message: Message, bot: Bot):
    s = int(db.load_state(message.from_user.id)[0])
    if s == 0:
        distance = get_distance(point_1, message)
        if distance < float(1000000000.0):
            current_state = str(1)
            rite_user_state(current_state, message)
            point_time('point1', message)
            id_picture = int(8)
            picture = db.get_picture(id_picture)[0]
            id_text = int(29)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene1_pic_list
            scene_text_list = scene1_text_list
            cur_id = 1
            scene_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 1:
        distance = get_distance(point_2, message)
        if distance < float(1000000000.0):
            current_state = str(2)
            scene_id = 2
            rite_user_state(current_state, message)
            point_time('point2', message)
            id_picture = int(7)
            picture = db.get_picture(id_picture)[0]
            id_text = int(25)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene2_pic_list
            scene_text_list = scene2_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 2:
        distance = get_distance(point_3, message)
        if distance < float(1000000000.0):
            current_state = str(3)
            scene_id = 3
            rite_user_state(current_state, message)
            point_time('point3', message)
            id_picture = int(9)
            picture = db.get_picture(id_picture)[0]
            id_text = int(30)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene3_pic_list
            scene_text_list = scene3_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 3:
        distance = get_distance(point_4, message)
        if distance < float(1000000000.0):
            current_state = str(4)
            scene_id = 4
            rite_user_state(current_state, message)
            point_time('point4', message)
            id_picture = int(22)
            picture = db.get_picture(id_picture)[0]
            id_text = int(66)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene4_pic_list
            scene_text_list = scene4_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 4:
        distance = get_distance(point_5, message)
        if distance < float(1000000000.0):
            current_state = str(5)
            scene_id = 5
            rite_user_state(current_state, message)
            point_time('point5', message)
            id_picture = int(30)
            picture = db.get_picture(id_picture)[0]
            id_text = int(86)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene5_pic_list
            scene_text_list = scene5_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 5:
        distance = get_distance(point_6, message)
        if distance < float(1000000000.0):
            current_state = str(6)
            scene_id = 6
            rite_user_state(current_state, message)
            point_time('point6', message)
            id_picture = int(3)
            picture = db.get_picture(id_picture)[0]
            id_text = int(99)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene6_pic_list
            scene_text_list = scene6_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 6:
        distance = get_distance(point_7, message)
        if distance < float(1000000000.0):
            current_state = str(7)
            scene_id = 7
            rite_user_state(current_state, message)
            point_time('point7', message)
            id_picture = int(2)
            picture = db.get_picture(id_picture)[0]
            id_text = int(117)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene7_pic_list
            scene_text_list = scene7_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 7:
        distance = get_distance(point_8, message)
        if distance < float(1000000000.0):
            current_state = str(8)
            scene_id = 8
            rite_user_state(current_state, message)
            point_time('point8', message)
            id_picture = int(49)
            picture = db.get_picture(id_picture)[0]
            id_text = int(127)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene8_pic_list
            scene_text_list = scene8_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 8:
        distance = get_distance(point_9, message)
        if distance < float(1000000000.0):
            current_state = str(9)
            scene_id = 9
            rite_user_state(current_state, message)
            point_time('point9', message)
            id_picture = int(2)
            picture = db.get_picture(id_picture)[0]
            id_text = int(141)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene9_pic_list
            scene_text_list = scene9_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 9:
        distance = get_distance(point_10, message)
        if distance < float(1000000000.0):
            current_state = str(10)
            scene_id = 10
            rite_user_state(current_state, message)
            point_time('point10', message)
            id_picture = int(64)
            picture = db.get_picture(id_picture)[0]
            id_text = int(157)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene10_pic_list
            scene_text_list = scene10_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 10:
        distance = get_distance(point_11, message)
        if distance < float(1000000000.0):
            current_state = str(11)
            scene_id = 11
            rite_user_state(current_state, message)
            point_time('point11', message)
            id_picture = int(3)
            picture = db.get_picture(id_picture)[0]
            id_text = int(195)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene11_pic_list
            scene_text_list = scene11_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 11:
        distance = get_distance(point_12, message)
        if distance < float(1000000000.0):
            current_state = str(12)
            scene_id = 12
            rite_user_state(current_state, message)
            point_time('point12', message)
            id_picture = int(3)
            picture = db.get_picture(id_picture)[0]
            id_text = int(200)
            text = db.get_text(id_text)[0]
            scene_pic_list = scene12_pic_list
            scene_text_list = scene12_text_list
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 12:
        distance = get_distance(point_13, message)
        if distance < float(1000000000.0):
            current_state = str(s+1)
            point_time('point13', message)
            scene_pic_list = scene13_pic_list
            scene_text_list = scene13_text_list
            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 13:
        distance = get_distance(point_14, message)
        if distance < float(1000000000.0):
            current_state = str(s+1)
            point_time('point14', message)
            scene_pic_list = scene14_pic_list
            scene_text_list = scene14_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 14:
        distance = get_distance(point_15, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point15', message)
            scene_pic_list = scene15_pic_list
            scene_text_list = scene15_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 15:
        distance = get_distance(point_16, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point16', message)
            scene_pic_list = scene16_pic_list
            scene_text_list = scene16_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 16:
        distance = get_distance(point_17, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point17', message)
            scene_pic_list = scene17_pic_list
            scene_text_list = scene17_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 17:
        distance = get_distance(point_18, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point18', message)
            scene_pic_list = scene18_pic_list
            scene_text_list = scene18_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 18:
        distance = get_distance(point_19, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point19', message)
            scene_pic_list = scene19_pic_list
            scene_text_list = scene19_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 19:
        distance = get_distance(point_20, message)
        if distance < float(1000000000.0):
            current_state = str(s + 1)
            point_time('point20', message)
            scene_pic_list = scene20_pic_list
            scene_text_list = scene20_text_list

            scene_id = int(current_state)
            rite_user_state(current_state, message)
            id_picture = int(scene_pic_list[0])
            picture = db.get_picture(id_picture)[0]
            id_text = int(scene_text_list[0])
            text = db.get_text(id_text)[0]
            cur_id = 1
            await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                                 reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
        else:
            distance = format(distance, '.2f')
            await bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')



