
from aiogram import Router
from .one_time_ikb_handlers import first_place_router, second_buy_router
from .navygation_kb_handler import navy_kb_router
from .purchase import purchase_router
from .up_inline import up_inline_router

inline_routers = Router()

inline_routers.include_routers(first_place_router, navy_kb_router, purchase_router, up_inline_router, second_buy_router)

