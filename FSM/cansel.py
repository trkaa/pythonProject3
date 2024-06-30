from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, Bot, F
from aiogram.types import Message
from keyboards import ikb_promo_input_start_ikb
from database import DataBase

cansel_fsm_router = Router()
db = DataBase()


@cansel_fsm_router.callback_query(F.data == 'cansel_fsm')
async def input_promo_code(message: Message, state: FSMContext, bot: Bot):
    user_id = message.from_user.id
    user_tuple = (message.from_user.id, message.from_user.full_name)
    if db.user_exist(user_id) is None:
        db.new_user(user_tuple)
    #state = db.load_state(message.from_user.id)[0]
    #if state is None:
    id_picture = int(113)
    picture = db.get_picture(id_picture)[0]
    await bot.send_photo(message.from_user.id, photo=picture, reply_markup=ikb_promo_input_start_ikb())
