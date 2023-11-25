from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import geo_kb

first_place_router = Router()


@first_place_router.callback_query(F.data == 'first_point')
async def show_first_point(message: Message, bot: Bot):
    point_1 = {"latitude": 55.107270, "longitude": 38.763697}

    await bot.send_location(message.from_user.id, latitude=point_1['latitude'], longitude=point_1['longitude'],
                            reply_markup=geo_kb())

# @main_handler.callback_query(Navigation.filter(F.menu == 'show'))
# async def show_id(callback: CallbackQuery, callback_data: Navigation, bot: Bot):
#     await callback.answer(text=f'ID этой фото: {callback_data.cur_id}', show_alert=True)
