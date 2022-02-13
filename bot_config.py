from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN = 'null'
admin_id = [416977980]


class Search(StatesGroup):
    object = State()
    s2 = State()

