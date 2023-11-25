from database import DataBase
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .callback import NavigationCB
from aiogram.types import Message, CallbackQuery

db = DataBase()


def navikeyboard(scene_pictures: list, scene_texts: list, cur_id: int):
    keyboard = InlineKeyboardBuilder()
    id_len = int(len(scene_texts))

    if cur_id == id_len:
        next_id = int(1)
        id_picture_f = str(scene_pictures[0])
        id_text_f = str(scene_texts[0])
        prev_id = cur_id - 1
        id_picture_p = str(scene_pictures[cur_id - 2])
        id_text_p = str(scene_texts[cur_id - 2])
        button_slide_p(keyboard, '<<<', prev_id, id_picture_p, id_text_p)
        button_slide_f(keyboard, '>>>', next_id, id_picture_f, id_text_f)

    elif cur_id == int(1):
        prev_id = id_len
        id_picture_p = str(scene_pictures[-1])
        id_text_p = str(scene_texts[-1])
        next_id = cur_id + 1
        id_picture_f = str(scene_pictures[cur_id])
        id_text_f = str(scene_texts[cur_id])
        button_slide_p(keyboard, '<<<', prev_id, id_picture_p, id_text_p)
        button_slide_f(keyboard, '>>>', next_id, id_picture_f, id_text_f)

    else:
        next_id = cur_id + 1
        prev_id = cur_id - 1
        id_picture_f = str(scene_pictures[cur_id])
        id_text_f = str(scene_texts[cur_id])
        id_picture_p = str(scene_pictures[cur_id - 2])
        id_text_p = str(scene_texts[cur_id - 2])
        button_slide_p(keyboard, '<<<', prev_id, id_picture_p, id_text_p)
        button_slide_f(keyboard, '>>>', next_id, id_picture_f, id_text_f)

    return keyboard.as_markup()


def button_slide_f(keyboard: InlineKeyboardBuilder, text: str, next_id: int, id_picture_f: str, id_text_f: str):
    keyboard.button(text=text, callback_data=NavigationCB(menu='navy', cur_id=next_id, picture_id=id_picture_f,
                                                          text_id=id_text_f))


def button_slide_p(keyboard: InlineKeyboardBuilder, text: str, prev_id: int, id_picture_p: str, id_text_p: str):
    keyboard.button(text=text, callback_data=NavigationCB(menu='navy', cur_id=prev_id, picture_id=id_picture_p,
                                                          text_id=id_text_p))

# def kb_navigation(total_size: int, current_id: int):
#     keyboard = InlineKeyboardBuilder()
#     prev_id = current_id - 1 if current_id != 0 else total_size - 1
#     next_id = current_id + 1 if current_id != total_size - 1 else 0
#     keyboard.button(text='<<<', callback_data=Navigation(menu='main', cur_id=prev_id))
#     keyboard.button(text='SHOW ID', callback_data=Navigation(menu='show', cur_id=current_id))
#     keyboard.button(text='>>>', callback_data=Navigation(menu='main', cur_id=next_id))
#     return keyboard.as_markup()
