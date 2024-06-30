import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.methods import DeleteWebhook
from settings import *
from database import DataBase
from handlers import handlers_routers
from FSM import all_fsm_routers
from handlers.inlinehandlers.purchase import process_pre_checkout_query, process_pay
from aiogram.types import ContentType

db = DataBase()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_routers(handlers_routers, all_fsm_routers)
dp.pre_checkout_query.register(process_pre_checkout_query)
dp.message.register(process_pay, F.content_type == ContentType.SUCCESSFUL_PAYMENT)


async def start_bot():
    try:
        db.create_table_check_points()
        db.create_table_text()
        db.create_table_pictures()
        print("DB connected...OK!")

    except:
        print('DB failure')

    dp.startup.register(on_start)
    dp.shutdown.register(on_shutdown)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
