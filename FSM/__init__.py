from aiogram import Router
from .sale import fsm_router
from .cansel import cansel_fsm_router

all_fsm_routers = Router()

all_fsm_routers.include_routers(fsm_router, cansel_fsm_router)
