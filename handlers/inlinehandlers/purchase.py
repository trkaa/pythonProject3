from os import getenv
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice, ContentType
from aiogram import Router, Bot, F
from aiogram.types import Message
from keyboards import ikb_first_point, navikeyboard
from database import DataBase
from aiogram.types import CallbackQuery
from functions import pay_time, insert_seller_table, rite_user_state, point_time
from lists import scene3_text_list, scene3_pic_list

db = DataBase()
purchase_router = Router()


@purchase_router.callback_query(F.data == 'final_sale')
async def purchase(callback: CallbackQuery, bot: Bot):
    user_id = callback.message.chat.id
    price = int(db.load_price(user_id)[0])
    prices = [LabeledPrice(label='квест', amount=price * 100)]
    await bot.send_invoice(chat_id=callback.message.chat.id,
                           title='государевы люди',
                           description='квест',
                           provider_token=getenv('P_TOKEN'),
                           currency='RUB',
                           prices=prices,
                           payload=f'{callback.message.from_user.full_name}',
                           start_parameter='final_sale')


async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def process_pay(message: Message, bot: Bot):
    pay_time(message)
    insert_seller_table(message)
    # state = db.load_state(message.from_user.id)[0]
    # current_state = str(0)
    # rite_user_state(current_state, message)
    # point_time('intro_checkpoint', message)
    # id_picture = int(1)
    # picture = db.get_picture(id_picture)[0]
    # id_text = int(1)
    # text = db.get_text(id_text)[0]
    # await bot.send_photo(message.from_user.id, photo=picture, caption=text)
    # await bot.send_message(message.from_user.id, text=db.get_text(20)[0], reply_markup=ikb_first_point())

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





