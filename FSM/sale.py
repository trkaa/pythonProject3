from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, Bot, F
from aiogram.types import Message
from database import DataBase
from keyboards import ikb_final_sale, cansel_fsm, navikeyboard
import os
from functions import pay_time, insert_seller_table, rite_user_state, point_time
from lists import scene3_text_list, scene3_pic_list

fsm_router = Router()
db = DataBase()

base_price = os.getenv('BASE_PRICE')


class Promo(StatesGroup):
    promo_input = State()


@fsm_router.callback_query(F.data == 'payments')
async def input_promo_code(message: Message, state: FSMContext, bot: Bot):
    await state.set_state(Promo.promo_input)
    await bot.send_message(message.from_user.id, text='введите промокод')


@fsm_router.message(Promo.promo_input)
async def save_promo_code(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(promo_code=message.text)
    code_list = list(db.load_code())
    for i in code_list:
        promo_code_new = await state.get_data()
        if str(i[0]) == str(promo_code_new.get('promo_code')):
            db.clear_code(i[1])
            if str(promo_code_new.get('promo_code')[:-6]) == 'any':
                coef = 10
                price = int(int(base_price) * (100 - coef) / 100)
                # user_price = (price, message.from_user.id)
                seller = str(promo_code_new.get('promo_code')[:-6])
                user_price_seller = (price, seller, message.from_user.id)
                # db.write_sell_price(user_price)
                db.write_sell_price_seller(user_price_seller)
                text = f'ваша цена {price} рублей'
                await state.clear()
                await bot.send_message(message.from_user.id, text=text, reply_markup=ikb_final_sale())

            if str(promo_code_new.get('promo_code')[:-6]) == 'free':
                await state.clear()
                price = int(0)
                seller = str(promo_code_new.get('promo_code')[:-6])
                user_price_seller = (price, seller, message.from_user.id)
                db.write_sell_price_seller(user_price_seller)
                pay_time(message)
                insert_seller_table(message)

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

            break
    else:
        await bot.send_message(message.from_user.id, text='такой промокод не существует, попробуйте другой',
                               reply_markup=cansel_fsm())
