from database import DataBase
from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from keyboards import NavigationCB, navikeyboard, HistoryReferenceCB, ref_navikeyboard, BackBTN
from lists import scene1_text_list, scene1_pic_list, sviblova_pic_list, sviblova_text_list, scene2_text_list, \
    scene2_pic_list, schemilovo_pic_list, schemilovo_text_list, scene3_text_list, scene3_pic_list, \
    pyatnica_gate_text_list, pyatnica_gate_pic_list, pischalnik_pic_list, pischalnik_text_list, scene4_pic_list, \
    scene4_text_list, krest_church_text_list, krest_church_pic_list, scene5_pic_list, scene5_text_list, \
    konung_palace_resurrection_church_pic_list, konung_palace_resurrection_church_text_list, scene6_pic_list, \
    scene6_text_list, uspenskiy_text_list, uspenskiy_pic_list, scene7_pic_list, scene7_text_list, kolokolnya_text_list,\
    kolokolnya_pic_list, scene8_pic_list, scene8_text_list, episcop_pic_list, episcop_text_list, scene9_text_list, \
    sad_text_list, scene9_pic_list, sad_pic_list, scene10_pic_list, scene10_text_list, bride_text_list, bride_pic_list,\
    scene11_text_list, scene11_pic_list, yamscaya_pic_list, yamscaya_text_list, scene12_text_list, scene12_pic_list, \
    kolomna_pic_list, kolomna_text_list, scene13_text_list, scene13_pic_list, ivanov_gate_text_list, \
    ivanov_gate_pic_list, scene14_pic_list, scene14_text_list, scene15_text_list, scene15_pic_list, reforma_pic_list, \
    reforma_text_list, stone_icon_text_list, stone_icon_pic_list, scene16_pic_list, scene16_text_list, brus_text_list, \
    brus_pic_list, scene17_pic_list, scene17_text_list, uspenia_pic_list, uspenia_text_list, scene18_text_list,\
    scene18_pic_list, gran_text_list, gran_pic_list, prison_text_list, prison_pic_list, scene19_text_list,\
    scene19_pic_list, marina_pic_list, marina_text_list, down_kolomna_text_list, down_kolomna_pic_list,\
    scene20_text_list, scene20_pic_list, vorotinskiy_text_list, vorotinskiy_pic_list, kosiye_text_list, kosiye_pic_list

from geo_points import point_2, point_3, point_4, point_5, point_6, point_7, point_8, point_9, point_10, point_11, \
    point_12, point_13, point_14, point_15, point_16, point_17, point_18, point_19, point_20

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
    if s == 2:
        scene_id = 2
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene2_pic_list
        scene_texts = scene2_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 3:
        scene_id = 3
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene3_pic_list
        scene_texts = scene3_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 4:
        scene_id = 4
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene4_pic_list
        scene_texts = scene4_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 5:
        scene_id = 5
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene5_pic_list
        scene_texts = scene5_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 6:
        scene_id = 6
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene6_pic_list
        scene_texts = scene6_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 7:
        scene_id = 7
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene7_pic_list
        scene_texts = scene7_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 8:
        scene_id = 8
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene8_pic_list
        scene_texts = scene8_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 9:
        scene_id = 9
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene9_pic_list
        scene_texts = scene9_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 10:
        scene_id = 10
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene10_pic_list
        scene_texts = scene10_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 11:
        scene_id = 11
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene11_pic_list
        scene_texts = scene11_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 12:
        scene_id = 12
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        scene_pictures = scene12_pic_list
        scene_texts = scene12_text_list
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 13:
        scene_id = s
        scene_pictures = scene13_pic_list
        scene_texts = scene13_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 14:
        scene_id = s
        scene_pictures = scene14_pic_list
        scene_texts = scene14_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 15:
        scene_id = s
        scene_pictures = scene15_pic_list
        scene_texts = scene15_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 16:
        scene_id = s
        scene_pictures = scene16_pic_list
        scene_texts = scene16_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 17:
        scene_id = s
        scene_pictures = scene17_pic_list
        scene_texts = scene17_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 18:
        scene_id = s
        scene_pictures = scene18_pic_list
        scene_texts = scene18_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 19:
        scene_id = s
        scene_pictures = scene19_pic_list
        scene_texts = scene19_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pictures, scene_texts, callback_data.cur_id,
                                                               scene_id))

    if s == 20:
        scene_id = s
        scene_pictures = scene20_pic_list
        scene_texts = scene20_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
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
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'schemilovo':
        picture = db.get_picture(7)[0]
        text = db.get_text(26)[0]
        ref_scene_pictures = schemilovo_pic_list
        ref_scene_texts = schemilovo_text_list
        cur_id = 1
        ref_scene = 'schemilovo'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'pyatnica':
        picture = db.get_picture(11)[0]
        text = db.get_text(43)[0]
        ref_scene_pictures = pyatnica_gate_pic_list
        ref_scene_texts = pyatnica_gate_text_list
        cur_id = 1
        ref_scene = 'pyatnica'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'pischalnik':
        picture = db.get_picture(16)[0]
        text = db.get_text(53)[0]
        ref_scene_pictures = pischalnik_pic_list
        ref_scene_texts = pischalnik_text_list
        cur_id = 1
        ref_scene = 'pischalnik'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'krest_church':
        picture = db.get_picture(17)[0]
        text = db.get_text(81)[0]
        ref_scene_pictures = krest_church_pic_list
        ref_scene_texts = krest_church_text_list
        cur_id = 1
        ref_scene = 'krest_church'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'konung_palace':
        picture = db.get_picture(23)[0]
        text = db.get_text(92)[0]
        ref_scene_pictures = konung_palace_resurrection_church_pic_list
        ref_scene_texts = konung_palace_resurrection_church_text_list
        cur_id = 1
        ref_scene = 'konung_palace'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'uspenskiy':
        picture = db.get_picture(31)[0]
        text = db.get_text(106)[0]
        ref_scene_pictures = uspenskiy_pic_list
        ref_scene_texts = uspenskiy_text_list
        cur_id = 1
        ref_scene = 'uspenskiy'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'kolokolnya':
        picture = db.get_picture(42)[0]
        text = db.get_text(120)[0]
        ref_scene_pictures = kolokolnya_pic_list
        ref_scene_texts = kolokolnya_text_list
        cur_id = 1
        ref_scene = 'kolokolnya'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'episcop':
        picture = db.get_picture(50)[0]
        text = db.get_text(130)[0]
        ref_scene_pictures = episcop_pic_list
        ref_scene_texts = episcop_text_list
        cur_id = 1
        ref_scene = 'episcop'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'sad':
        picture = db.get_picture(61)[0]
        text = db.get_text(150)[0]
        ref_scene_pictures = sad_pic_list
        ref_scene_texts = sad_text_list
        cur_id = 1
        ref_scene = 'sad'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'bride':
        picture = db.get_picture(62)[0]
        text = db.get_text(160)[0]
        ref_scene_pictures = bride_pic_list
        ref_scene_texts = bride_text_list
        cur_id = 1
        ref_scene = 'bride'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'yamscaya':
        picture = db.get_picture(65)[0]
        text = db.get_text(197)[0]
        ref_scene_pictures = yamscaya_pic_list
        ref_scene_texts = yamscaya_text_list
        cur_id = 1
        ref_scene = 'yamscaya'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'kolomna':
        picture = db.get_picture(66)[0]
        text = db.get_text(205)[0]
        ref_scene_pictures = kolomna_pic_list
        ref_scene_texts = kolomna_text_list
        cur_id = 1
        ref_scene = 'kolomna'
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'ivanovskie':
        ref_scene_pictures = ivanov_gate_pic_list
        ref_scene_texts = ivanov_gate_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'reforma':
        ref_scene_pictures = reforma_pic_list
        ref_scene_texts = reforma_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'stone':
        ref_scene_pictures = stone_icon_pic_list
        ref_scene_texts = stone_icon_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'brus':
        ref_scene_pictures = brus_pic_list
        ref_scene_texts = brus_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'uspenia':
        ref_scene_pictures = uspenia_pic_list
        ref_scene_texts = uspenia_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'gran':
        ref_scene_pictures = gran_pic_list
        ref_scene_texts = gran_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'marina':
        ref_scene_pictures = marina_pic_list
        ref_scene_texts = marina_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'down':
        ref_scene_pictures = down_kolomna_pic_list
        ref_scene_texts = down_kolomna_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'prison':
        ref_scene_pictures = prison_pic_list
        ref_scene_texts = prison_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'kosiye':
        ref_scene_pictures = kosiye_pic_list
        ref_scene_texts = kosiye_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))

    if callback_data.reference_name == 'vorotinskiy':
        ref_scene_pictures = vorotinskiy_pic_list
        ref_scene_texts = vorotinskiy_text_list

        picture = db.get_picture(ref_scene_pictures[0])[0]
        text = db.get_text(ref_scene_texts[0])[0]
        cur_id = 1
        ref_scene = callback_data.reference_name
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts, cur_id,
                                                                   ref_scene))


@navy_kb_router.callback_query(NavigationCB.filter(F.menu))
async def reference_navi_bar(callback: CallbackQuery, callback_data: NavigationCB, bot: Bot):
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

    if callback_data.menu == 'schemilovo':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = schemilovo_pic_list
        ref_scene_texts = schemilovo_text_list
        ref_scene = 'schemilovo'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'pyatnica':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = pyatnica_gate_pic_list
        ref_scene_texts = pyatnica_gate_text_list
        ref_scene = 'pyatnica'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'pischalnik':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = pischalnik_pic_list
        ref_scene_texts = pischalnik_text_list
        ref_scene = 'pischalnik'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'krest_church':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = krest_church_pic_list
        ref_scene_texts = krest_church_text_list
        ref_scene = 'krest_church'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'konung_palace':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = konung_palace_resurrection_church_pic_list
        ref_scene_texts = konung_palace_resurrection_church_text_list
        ref_scene = 'konung_palace'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'uspenskiy':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = uspenskiy_pic_list
        ref_scene_texts = uspenskiy_text_list
        ref_scene = 'uspenskiy'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'kolokolnya':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = kolokolnya_pic_list
        ref_scene_texts = kolokolnya_text_list
        ref_scene = 'kolokolnya'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'episcop':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = episcop_pic_list
        ref_scene_texts = episcop_text_list
        ref_scene = 'episcop'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'sad':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = sad_pic_list
        ref_scene_texts = sad_text_list
        ref_scene = 'sad'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'bride':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = bride_pic_list
        ref_scene_texts = bride_text_list
        ref_scene = 'bride'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'yamscaya':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = yamscaya_pic_list
        ref_scene_texts = yamscaya_text_list
        ref_scene = 'yamscaya'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'kolomna':
        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene_pictures = kolomna_pic_list
        ref_scene_texts = kolomna_text_list
        ref_scene = 'kolomna'
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'ivanovskie':
        ref_scene_pictures = ivanov_gate_pic_list
        ref_scene_texts = ivanov_gate_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'reforma':
        ref_scene_pictures = reforma_pic_list
        ref_scene_texts = reforma_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'stone':
        ref_scene_pictures = stone_icon_pic_list
        ref_scene_texts = stone_icon_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'brus':
        ref_scene_pictures = brus_pic_list
        ref_scene_texts = brus_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'uspenia':
        ref_scene_pictures = uspenia_pic_list
        ref_scene_texts = uspenia_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'gran':
        ref_scene_pictures = gran_pic_list
        ref_scene_texts = gran_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'marina':
        ref_scene_pictures = marina_pic_list
        ref_scene_texts = marina_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'down':
        ref_scene_pictures = down_kolomna_pic_list
        ref_scene_texts = down_kolomna_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'prison':
        ref_scene_pictures = prison_pic_list
        ref_scene_texts = prison_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'kosiye':
        ref_scene_pictures = kosiye_pic_list
        ref_scene_texts = kosiye_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))

    if callback_data.menu == 'vorotinskiy':
        ref_scene_pictures = vorotinskiy_pic_list
        ref_scene_texts = vorotinskiy_text_list

        id_picture = int(callback_data.picture_id)
        picture = db.get_picture(id_picture)[0]
        id_text = int(callback_data.text_id)
        text = db.get_text(id_text)[0]
        ref_scene = callback_data.menu
        photo = InputMediaPhoto(media=picture,
                                caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=ref_navikeyboard(ref_scene_pictures, ref_scene_texts,
                                                                   callback_data.cur_id, ref_scene))


@navy_kb_router.callback_query(BackBTN.filter(F.back == 'reference_back'))
async def reference_back_button(callback: CallbackQuery, bot: Bot):
    s = int(db.load_state(callback.from_user.id)[0])
    if s == 1:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene1_pic_list
        scene_text_list = scene1_text_list
        cur_id = 13
        scene_id = 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 2:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene2_pic_list
        scene_text_list = scene2_text_list
        cur_id = 2
        scene_id = 2
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 3:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene3_pic_list
        scene_text_list = scene3_text_list
        cur_id = 14
        scene_id = 3
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 4:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene4_pic_list
        scene_text_list = scene4_text_list
        cur_id = 16
        scene_id = 4
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 5:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene5_pic_list
        scene_text_list = scene5_text_list
        cur_id = 7
        scene_id = 5
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 6:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene6_pic_list
        scene_text_list = scene6_text_list
        cur_id = 7
        scene_id = 6
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 7:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene7_pic_list
        scene_text_list = scene7_text_list
        cur_id = 4
        scene_id = 7
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 8:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene8_pic_list
        scene_text_list = scene8_text_list
        cur_id = 4
        scene_id = 8
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 9:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene9_pic_list
        scene_text_list = scene9_text_list
        cur_id = 10
        scene_id = 9
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 10:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene10_pic_list
        scene_text_list = scene10_text_list
        cur_id = 4
        scene_id = 10
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 11:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene11_pic_list
        scene_text_list = scene11_text_list
        cur_id = 3
        scene_id = 11
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 12:
        id_picture = int(4)
        picture = db.get_picture(id_picture)[0]
        id_text = int(9)
        text = db.get_text(id_text)[0]
        scene_pic_list = scene12_pic_list
        scene_text_list = scene12_text_list
        cur_id = 6
        scene_id = 12
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 13:
        scene_id = s
        scene_pic_list = scene13_pic_list
        scene_text_list = scene13_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 15:
        scene_id = s
        scene_pic_list = scene15_pic_list
        scene_text_list = scene15_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 16:
        scene_id = s
        scene_pic_list = scene16_pic_list
        scene_text_list = scene16_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 17:
        scene_id = s
        scene_pic_list = scene17_pic_list
        scene_text_list = scene17_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 18:
        scene_id = s
        scene_pic_list = scene18_pic_list
        scene_text_list = scene18_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 19:
        scene_id = s
        scene_pic_list = scene19_pic_list
        scene_text_list = scene19_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))

    if s == 20:
        scene_id = s
        scene_pic_list = scene20_pic_list
        scene_text_list = scene20_text_list

        id_picture = int(scene_pic_list[-2])
        picture = db.get_picture(id_picture)[0]
        id_text = int(scene_text_list[-2])
        text = db.get_text(id_text)[0]
        cur_id = (scene_text_list.index(scene_text_list[-2])) + 1
        photo = InputMediaPhoto(media=picture, caption=text)
        await bot.edit_message_media(media=photo, chat_id=callback.message.chat.id,
                                     message_id=callback.message.message_id,
                                     reply_markup=navikeyboard(scene_pic_list, scene_text_list, cur_id, scene_id))


@navy_kb_router.callback_query(BackBTN.filter(F.back))
async def reference_keyboard_audio_load_button(callback: CallbackQuery, callback_data: BackBTN, bot: Bot):
    if callback_data.back == 'sviblova':
        audio = 'CQACAgIAAxkBAAIBZWViSieiVOcoiyEIruPxsPlBM_8qAAKwQwAC2IoQSwx5s-rtZBClMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'schemilovo':
        audio = 'CQACAgIAAxkBAAICuWVpC_0XjYwIHoOUqQTPZ4ONVuWdAAJlNgACnFhIS0Xil75ICtxzMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'pyatnica':
        audio = 'CQACAgIAAxkBAAIC_2VqHaoS4rMEuXYqt_CvzLiwGyQMAAJmPQACnFhQS0dM3Y6GMMeEMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'pischalnik':
        audio = 'CQACAgIAAxkBAAIDD2VqKhZnW7ot4FYqrYtRYheRV2A8AALtPQACnFhQS3MCUepDL4mhMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'krest_church':
        audio = 'CQACAgIAAxkBAAIDJWVqfrSav5TuglxaNB1HvM5GyDsxAAJiPwACnFhQS6luBp-JEPCAMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'konung_palace':
        audio = 'CQACAgIAAxkBAAIDWmVrdsiHgHEkYnsevsT3WBddBUqAAAJWPAACm59gSyaqwlq5YrReMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'uspenskiy':
        audio = 'CQACAgIAAxkBAAIDjmVrm3_Qydr9gq26zaj3Iql6pq2CAAJePwACm59gSwLkJ7M7_eK_MwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'kolokolnya':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'episcop':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'sad':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'bride':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'yamscaya':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'kolomna':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'ivanovskie':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'stone':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'reforma':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'brus':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'uspenia':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'gran':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'marina':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)
    if callback_data.back == 'down':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'prison':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'kosiye':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)

    if callback_data.back == 'vorotinskiy':
        audio = 'CQACAgIAAxkBAAID_GVsvrmfHn5alkyMAU8r9tLlXgK7AAKvQAACledoS4L-MSmFn18LMwQ'
        await bot.send_audio(audio=audio, chat_id=callback.message.chat.id)


@navy_kb_router.callback_query(F.data == 'location')
async def show_next_point(callback: CallbackQuery, bot: Bot):
    s = int(db.load_state(callback.from_user.id)[0])
    if s == 1:
        await bot.send_location(callback.from_user.id, latitude=point_2['latitude'], longitude=point_2['longitude'])

    if s == 2:
        await bot.send_location(callback.from_user.id, latitude=point_3['latitude'], longitude=point_3['longitude'])

    if s == 3:
        await bot.send_location(callback.from_user.id, latitude=point_4['latitude'], longitude=point_4['longitude'])

    if s == 4:
        await bot.send_location(callback.from_user.id, latitude=point_5['latitude'], longitude=point_5['longitude'])

    if s == 5:
        await bot.send_location(callback.from_user.id, latitude=point_6['latitude'], longitude=point_6['longitude'])

    if s == 6:
        await bot.send_location(callback.from_user.id, latitude=point_7['latitude'], longitude=point_7['longitude'])

    if s == 7:
        await bot.send_location(callback.from_user.id, latitude=point_8['latitude'], longitude=point_8['longitude'])

    if s == 8:
        await bot.send_location(callback.from_user.id, latitude=point_9['latitude'], longitude=point_9['longitude'])

    if s == 9:
        await bot.send_location(callback.from_user.id, latitude=point_10['latitude'], longitude=point_10['longitude'])

    if s == 10:
        await bot.send_location(callback.from_user.id, latitude=point_11['latitude'], longitude=point_11['longitude'])

    if s == 11:
        await bot.send_location(callback.from_user.id, latitude=point_12['latitude'], longitude=point_12['longitude'])

    if s == 12:
        await bot.send_location(callback.from_user.id, latitude=point_13['latitude'], longitude=point_13['longitude'])

    if s == 13:
        await bot.send_location(callback.from_user.id, latitude=point_14['latitude'], longitude=point_14['longitude'])

    if s == 14:
        await bot.send_location(callback.from_user.id, latitude=point_15['latitude'], longitude=point_15['longitude'])

    if s == 15:
        await bot.send_location(callback.from_user.id, latitude=point_16['latitude'], longitude=point_16['longitude'])

    if s == 16:
        await bot.send_location(callback.from_user.id, latitude=point_17['latitude'], longitude=point_17['longitude'])

    if s == 17:
        await bot.send_location(callback.from_user.id, latitude=point_18['latitude'], longitude=point_18['longitude'])

    if s == 18:
        await bot.send_location(callback.from_user.id, latitude=point_19['latitude'], longitude=point_19['longitude'])

    if s == 19:
        await bot.send_location(callback.from_user.id, latitude=point_20['latitude'], longitude=point_20['longitude'])
