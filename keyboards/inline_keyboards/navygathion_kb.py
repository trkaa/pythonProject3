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
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'справка по Свибловой башне', reference_name='sviblova')
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

    if scene_id == 2:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'справка по Щемиловской башне', reference_name='schemilovo')
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
    if scene_id == 3:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'справка по пищальникам', reference_name='pischalnik')
            reference_button(keyboard, 'справка по Пятницкой башне', reference_name='pyatnica')
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 1, 2)

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

    if scene_id == 4:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'легенда крестовоздвиженской церкви', reference_name='krest_church')
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

    if scene_id == 5:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'княжеский дворец и воскресенская церковь',
                             reference_name='konung_palace')
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

    if scene_id == 6:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'успенский собор',
                             reference_name='uspenskiy')
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

    if scene_id == 7:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'успенская шатровая колокольня',
                             reference_name='kolokolnya')
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

    if scene_id == 8:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'епископский дворец',
                             reference_name='episcop')
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

    if scene_id == 9:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'яблоневые сады',
                             reference_name='sad')
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

    if scene_id == 10:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Коломенские жёны Ивана Грозного',
                             reference_name='bride')
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

    if scene_id == 11:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Ямская башня',
                             reference_name='yamscaya')
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

    if scene_id == 12:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'источники богатства Коломны',
                             reference_name='kolomna')
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

    if scene_id == 13:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Ивановские ворота',
                             reference_name='ivanovskie')
            reference_button(keyboard, 'каменная икона',
                             reference_name='stone')
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 1, 2)

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

    if scene_id == 14:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            # reference_button(keyboard, 'Ивановские ворота',
            #                  reference_name='ivanovskie')
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(2)

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

    if scene_id == 15:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'военная реформа Ивана IV',
                             reference_name='reforma')
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

    if scene_id == 16:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Брусенский монастырь',
                             reference_name='brus')
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

    if scene_id == 17:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Церковь Успения Пресвятой Богородицы',
                             reference_name='uspenia')
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

    if scene_id == 18:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'грановитая башня',
                             reference_name='gran')
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

    if scene_id == 19:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            location_button(keyboard)
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Маринкина башня',
                             reference_name='marina')
            reference_button(keyboard, 'взятия Коломны',
                             reference_name='down')
            reference_button(keyboard, 'Коломна как тюрьма',
                             reference_name='prison')
            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 1, 1, 2)

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

    if scene_id == 20:
        if cur_id == id_len:
            next_id = int(1)
            id_picture_f = str(scene_pictures[0])
            id_text_f = str(scene_texts[0])
            prev_id = cur_id - 1
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Маринкина башня',
                             reference_name='marina')
            reference_button(keyboard, 'взятия Коломны',
                             reference_name='down')
            reference_button(keyboard, 'Коломна как тюрьма',
                             reference_name='prison')
            reference_button(keyboard, 'грановитая башня',
                             reference_name='gran')
            reference_button(keyboard, 'Церковь Успения Пресвятой Богородицы',
                             reference_name='uspenia')
            reference_button(keyboard, 'Брусенский монастырь',
                             reference_name='brus')
            reference_button(keyboard, 'военная реформа Ивана IV',
                             reference_name='reforma')
            reference_button(keyboard, 'Ивановские ворота',
                             reference_name='ivanovskie')
            reference_button(keyboard, 'каменная икона',
                             reference_name='stone')
            reference_button(keyboard, 'источники богатства Коломны',
                             reference_name='kolomna')
            reference_button(keyboard, 'Ямская башня',
                             reference_name='yamscaya')
            reference_button(keyboard, 'Коломенские жёны Ивана Грозного',
                             reference_name='bride')
            reference_button(keyboard, 'яблоневые сады',
                             reference_name='sad')
            reference_button(keyboard, 'епископский дворец',
                             reference_name='episcop')
            reference_button(keyboard, 'успенская шатровая колокольня',
                             reference_name='kolokolnya')
            reference_button(keyboard, 'успенский собор',
                             reference_name='uspenskiy')
            reference_button(keyboard, 'княжеский дворец и воскресенская церковь',
                             reference_name='konung_palace')
            reference_button(keyboard, 'легенда крестовоздвиженской церкви', reference_name='krest_church')
            reference_button(keyboard, 'справка по пищальникам', reference_name='pischalnik')
            reference_button(keyboard, 'справка по Пятницкой башне', reference_name='pyatnica')
            reference_button(keyboard, 'справка по Щемиловской башне', reference_name='schemilovo')
            reference_button(keyboard, 'справка по Свибловой башне', reference_name='sviblova')

            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)

        elif cur_id == (id_len - 1):
            next_id = cur_id + 1
            prev_id = cur_id - 1
            id_picture_f = str(scene_pictures[cur_id])
            id_text_f = str(scene_texts[cur_id])
            id_picture_p = str(scene_pictures[cur_id - 2])
            id_text_p = str(scene_texts[cur_id - 2])
            menu = 'navy'
            reference_button(keyboard, 'Косые ворота',
                             reference_name='kosiye')
            reference_button(keyboard, 'Михаил Иванович Воротынский ',
                             reference_name='vorotinskiy')

            button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
            button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)
            keyboard.adjust(1, 1, 2)

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


def location_button(keyboard: InlineKeyboardBuilder):
    keyboard.button(text='следующая локация', callback_data='location')


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
        button_slide_p(keyboard, '<<<', menu, prev_id, id_picture_p, id_text_p)
        back_reference_button(keyboard, 'назад')
        button_slide_f(keyboard, '>>>', menu, next_id, id_picture_f, id_text_f)

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
