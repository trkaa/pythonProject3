from aiogram import Router
from .start import start_router
from .geo_handler import geo_router
from .help import help_router
from .up import up_router

usual_routers = Router()

usual_routers.include_routers(start_router, geo_router, help_router, up_router)
