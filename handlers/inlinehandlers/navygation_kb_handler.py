from database import DataBase
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from keyboards import NavigationCB, navikeyboard

db = DataBase()
navy_kb_router = Router()


@navy_kb_router.callback_query(NavigationCB.filter(F.menu == 'navy'))
async def navi_bar(callback: CallbackQuery, callback_data: NavigationCB, bot: Bot):
    id_picture = int(callback_data.picture_id)
    picture = db.get_picture(id_picture)[0]
    id_text = int(callback_data.text_id)
    text = db.get_text(id_text)[0]
    scene1_pic_list = [2, 3, 2, 3, 2, 3, 2]
    scene1_text_list = [2, 3, 4, 5, 6, 7, 8]
    # scene_cur_id = int(callback_data.cur_id)
    print(id_picture)
    print(id_text)
    # print(scene_cur_id)
    print(picture)

    photo = InputMediaPhoto(media=picture,
                            caption=text)
    await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 reply_markup=navikeyboard(scene1_pic_list, scene1_text_list, callback_data.cur_id))
