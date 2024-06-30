from aiogram import Bot, Router, F
from aiogram.types import Message
from database import DataBase
from keyboards import geo_kb, ikb_promo_input_start_ikb
from geo_points import point_1

first_place_router = Router()
second_buy_router = Router()
db = DataBase()


@first_place_router.callback_query(F.data == 'first_point')
async def show_first_point(message: Message, bot: Bot):
    s = int(db.load_state(message.from_user.id)[0])
    if s == 0:
        await bot.send_location(message.from_user.id, latitude=point_1['latitude'], longitude=point_1['longitude'],
                                reply_markup=geo_kb())
    else:
        pass


@second_buy_router.callback_query(F.data == 'input_pay')
async def second_buy_promo(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text='введите промокод', reply_markup=ikb_promo_input_start_ikb())

# @main_handler.callback_query(Navigation.filter(F.menu == 'show'))
# async def show_id(callback: CallbackQuery, callback_data: Navigation, bot: Bot):
#     await callback.answer(text=f'ID этой фото: {callback_data.cur_id}', show_alert=True)
