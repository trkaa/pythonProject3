from aiogram.filters.callback_data import CallbackData


class NavigationCB(CallbackData, prefix='types'):
    menu: str
    cur_id: int
    picture_id: str
    text_id: str


class HistoryReferenceCB(CallbackData, prefix='reference'):
    menu: str
    reference_name: str


class BackBTN(CallbackData, prefix='backbtn'):
    back: str

# class UserCB(CallbackData, prefix='user'):
#     button: str
#     user_id: int
#
#
# class ConfirmCB(CallbackData, prefix='confirm'):
#     menu: str
#     button: str
#
#
# class BasketCB(CallbackData, prefix='basket'):
#     menu: str
#     u_id: int
#
#
# class MainMenuCB(CallbackData, prefix='main_menu'):
#     button: str
#     user_id: int = 0
