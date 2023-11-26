from database import DataBase
from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from keyboards import NavigationCB, navikeyboard, HistoryReferenceCB, ref_navikeyboard, BackBTN
from lists import scene1_text_list, scene1_pic_list, sviblova_pic_list, sviblova_text_list

db = DataBase()
navy_kb_router = Router()


@navy_kb_router.callback_query(NavigationCB.filter(F.menu == 'navy'))
async def navi_bar(callback: CallbackQuery, callback_data: NavigationCB, bot: Bot):
    s = int(db.load_state(callback.from_user.id)[0])
    if s == 1:
        scene_id = 1
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene1_pic_list
        scene_texts = scene1_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))


@navy_kb_router.callback_query(HistoryReferenceCB.filter(F.menu == 'reference'))
async def ref_button(callback: CallbackQuery, callback_data: HistoryReferenceCB, bot: Bot):
    if callback_data.reference_name == 'sviblova':
        picture = db.get_picture(5)[0]
        text = db.get_text(10)[0]
        ref_scene_pictures = sviblova_pic_list
        ref_scene_texts = sviblova_text_list
        cur_id = 1
        ref_scene = 'sviblova'
        # audio = 'CQACAgIAAxkBAAIBZWViSieiVOcoiyEIruPxsPlBM_8qAAKwQwAC2IoQSwx5s-rtZBClMwQ'
        # await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))


@navy_kb_router.callback_query(NavigationCB.filter(F.menu))
async def navi_bar(callback: CallbackQuery, callback_data: NavigationCB, bot: Bot):
    if callback_data.menu == 'sviblova':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = sviblova_pic_list
        ref_scene_texts = sviblova_text_list
        ref_scene = 'sviblova'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))


@navy_kb_router.callback_query(BackBTN.filter(F.back == 'reference_back'))
async def navi_bar(callback: CallbackQuery, bot: Bot):
    s = int(db.load_state(callback.from_user.id)[0])
    if s == 1:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene1_pic_list
        scene_text_list = scene1_text_list
        cur_id = 8
        scene_id = 1
        photo = InputMediaPhoto(media=picture, caption=text)

        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))


@navy_kb_router.callback_query(BackBTN.filter(F.back == 'sviblova'))
async def navi_bar(callback: CallbackQuery, bot: Bot):
    audio = 'CQACAgIAAxkBAAIBZWViSieiVOcoiyEIruPxsPlBM_8qAAKwQwAC2IoQSwx5s-rtZBClMwQ'
    await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)
