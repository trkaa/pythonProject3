from database import DataBase
from aiogram.types import Message
from aiogram import Router, Bot
from aiogram.filters import Command

db = DataBase()
help_router = Router()


@help_router.message(Command('help'))
async def mes_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text=db.get_text(336)[0])

