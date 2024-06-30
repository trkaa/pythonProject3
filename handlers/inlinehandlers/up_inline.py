from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot, F
from keyboards import navikeyboard, geo_kb
from geo_points import point_1
from lists import scene1_pic_list, scene1_text_list, scene2_pic_list, scene2_text_list, scene3_pic_list, \
    scene3_text_list, scene4_text_list, scene4_pic_list, scene5_text_list, scene5_pic_list, scene6_text_list, \
    scene6_pic_list, scene7_text_list, scene7_pic_list, scene8_text_list, scene8_pic_list, scene9_text_list, \
    scene9_pic_list, scene10_text_list, scene10_pic_list, scene11_pic_list, scene11_text_list, scene12_pic_list, \
    scene12_text_list, scene13_pic_list, scene13_text_list, scene14_pic_list, scene14_text_list, scene15_pic_list, \
    scene15_text_list, scene16_text_list, scene16_pic_list, scene17_pic_list, scene17_text_list, scene18_pic_list, \
    scene18_text_list, scene19_pic_list, scene19_text_list, scene20_pic_list, scene20_text_list

db = DataBase()
up_inline_router = Router()


@up_inline_router.callback_query(F.data == 'up')
async def up_bot(message: Message, bot: Bot):
    s = int(db.load_state(message.from_user.id)[0])
    if s == 0:
        await bot.send_location(message.from_user.id, latitude=point_1['latitude'], longitude=point_1['longitude'],
                                reply_markup=geo_kb())

    if s == 1:
        current_state = str(s)
        scene_pic_list = scene1_pic_list
        scene_text_list = scene1_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 2:
        current_state = str(s)
        scene_pic_list = scene2_pic_list
        scene_text_list = scene2_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 3:
        current_state = str(s)
        scene_pic_list = scene3_pic_list
        scene_text_list = scene3_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 4:
        current_state = str(s)
        scene_pic_list = scene4_pic_list
        scene_text_list = scene4_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 5:
        current_state = str(s)
        scene_pic_list = scene5_pic_list
        scene_text_list = scene5_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 6:
        current_state = str(s)
        scene_pic_list = scene6_pic_list
        scene_text_list = scene6_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 7:
        current_state = str(s)
        scene_pic_list = scene7_pic_list
        scene_text_list = scene7_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1

        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 8:
        current_state = str(s)
        scene_pic_list = scene8_pic_list
        scene_text_list = scene8_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 9:
        current_state = str(s)
        scene_pic_list = scene9_pic_list
        scene_text_list = scene9_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 10:
        current_state = str(s)
        scene_pic_list = scene10_pic_list
        scene_text_list = scene10_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 11:
        current_state = str(s)
        scene_pic_list = scene11_pic_list
        scene_text_list = scene11_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 12:
        current_state = str(s)
        scene_pic_list = scene12_pic_list
        scene_text_list = scene12_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 13:
        current_state = str(s)
        scene_pic_list = scene13_pic_list
        scene_text_list = scene13_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 14:
        current_state = str(s)

        scene_pic_list = scene14_pic_list
        scene_text_list = scene14_text_list

        scene_id = int(current_state)

        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 15:
        current_state = str(s)

        scene_pic_list = scene15_pic_list
        scene_text_list = scene15_text_list

        scene_id = int(current_state)

        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 16:
        current_state = str(s)

        scene_pic_list = scene16_pic_list
        scene_text_list = scene16_text_list

        scene_id = int(current_state)

        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 17:
        current_state = str(s)

        scene_pic_list = scene17_pic_list
        scene_text_list = scene17_text_list

        scene_id = int(current_state)

        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 18:
        current_state = str(s)

        scene_pic_list = scene18_pic_list
        scene_text_list = scene18_text_list

        scene_id = int(current_state)

        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 19:
        current_state = str(s)
        scene_pic_list = scene19_pic_list
        scene_text_list = scene19_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 20:
        current_state = str(s)
        scene_pic_list = scene20_pic_list
        scene_text_list = scene20_text_list
        scene_id = int(current_state)
        id_picture = int(scene_pic_list[0])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[0])
        text = db.get_text(id_text)[0]
        cur_id = 1
        await bot.send_photo(message.from_user.id, photo=picture, caption=text,
                             reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))
