from aiogram import Router
from .inlinehandlers import inline_routers
from .usual_handlers import usual_routers

handlers_routers = Router()

handlers_routers.include_routers(usual_routers, inline_routers)
