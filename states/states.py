from aiogram.dispatcher.filters.state import State, StatesGroup


class Game(StatesGroup):
    END = State()
