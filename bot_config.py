from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN = '1179370638:AAFCdTktKJ6h-FNW6z-q2SDjXoSGdY2pW3w'
admin_id = [416977980, 381365580]


class Search(StatesGroup):
    object = State()
    s2 = State()

