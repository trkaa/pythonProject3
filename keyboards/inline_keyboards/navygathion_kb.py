from database import DataBase
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback import NavigationCB, HistoryReferenceCB, BackBTN

db = DataBase()


def navikeyboard(scene_pictures: list, scene_texts: list, cur_id: int, scene_id: int):
    keyboard = InlineKeyboardBuilder()
    id_len = int(len(scene_texts))
    if scene_id == 1:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            # sviblova_pic_id = 5
            # sviblova_text_id = 10
            # reference_button(keyboard, 'справка по свибловой башне', cur_id, sviblova_pic_id, sviblova_text_id)
            reference_button(keyboard, 'справка по свибловой башне', reference_name='sviblova')
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == int(1):
            prev_id = id_len
            id_picture_p = str(scene_pictures[-1])
            id_text_p = str(scene_texts[-1])
            next_id = cur_id + 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            menu = 'navy'

            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)

        else:
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)

        return keyboard.as_markup()


def button_slide_f(keyboard: InlineKeyboardBuilder, text: str, menu: str, next_id: int, id_picture_f: str,
                   id_text_f: str):
    keyboard.button(text=text, callback_data=NavigationCB(menu=menu, cur_id=next_id, picture_id=id_picture_f,
                                                          text_id=id_text_f))


def button_slide_p(keyboard: InlineKeyboardBuilder, text: str, menu: str, prev_id: int, id_picture_p: str,
                   id_text_p: str):
    keyboard.button(text=text, callback_data=NavigationCB(menu=menu, cur_id=prev_id, picture_id=id_picture_p,
                                                          text_id=id_text_p))


def reference_button(keyboard: InlineKeyboardBuilder, text: str, reference_name: str):
    keyboard.button(text=text, callback_data=HistoryReferenceCB(menu='reference', reference_name=reference_name))


def back_reference_button(keyboard: InlineKeyboardBuilder, text: str):
    keyboard.button(text=text, callback_data=BackBTN(back='reference_back'))


def reference_audio_load(keyboard: InlineKeyboardBuilder, text: str, back: str):
    keyboard.button(text=text, callback_data=BackBTN(back=back))


def ref_navikeyboard(ref_scene_pictures: list, ref_scene_texts: list, cur_id: int, ref_scene: str):
    keyboard = InlineKeyboardBuilder()
    id_len = int(len(ref_scene_texts))
    if cur_id == id_len:
        next_id = int(1)
        id_picture_f = str(ref_scene_pictures[0])
        id_text_f = str(ref_scene_texts[0])
        prev_id = cur_id - 1
        id_picture_p = str(ref_scene_pictures[cur_id - 2])
        id_text_p = str(ref_scene_texts[cur_id - 2])
        menu = ref_scene
        # sviblova_pic_id = 5
        # sviblova_text_id = 10
        # reference_button(keyboard, 'справка по свибловой башне', cur_id, sviblova_pic_id, sviblova_text_id)
        # reference_button(keyboard, 'справка по свибловой башне', reference_name='sviblova')
        button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
        back_reference_button(keyboard, 'назад')
        button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
        # keyboard.adjust(1, 2)

    elif cur_id == int(1):
        prev_id = id_len
        id_picture_p = str(ref_scene_pictures[-1])
        id_text_p = str(ref_scene_texts[-1])
        next_id = cur_id + 1
        id_picture_f = str(ref_scene_pictures[cur_id])
        id_text_f = str(ref_scene_texts[cur_id])
        menu = ref_scene
        back = ref_scene
        reference_audio_load(keyboard, 'загрузить аудио', back=back)
        button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
        back_reference_button(keyboard, 'назад')
        button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
        keyboard.adjust(1, 3)

    else:
        next_id = cur_id + 1
        prev_id = cur_id - 1
        id_picture_f = str(ref_scene_pictures[cur_id])
        id_text_f = str(ref_scene_texts[cur_id])
        id_picture_p = str(ref_scene_pictures[cur_id - 2])
        id_text_p = str(ref_scene_texts[cur_id - 2])
        menu = ref_scene
        button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
        back_reference_button(keyboard, 'назад')
        button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)

    return keyboard.as_markup()

# def kb_navigation(total_size: int, current_id: int):
#     keyboard = InlineKeyboardBuilder()
#     prev_id = current_id - 1 if current_id != 0 else total_size - 1
#     next_id = current_id + 1 if current_id != total_size - 1 else 0
#     keyboard.button(text='<<<', callback_data=Navigation(menu='main', cur_id=prev_id))
#     keyboard.button(text='SHOW ID', callback_data=Navigation(menu='show', cur_id=current_id))
#     keyboard.button(text='>>>', callback_data=Navigation(menu='main', cur_id=next_id))
#     return keyboard.as_markup()
