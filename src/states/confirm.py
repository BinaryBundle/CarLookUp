from aiogram.dispatcher.filters.state import State, StatesGroup


class ConfirmationAccount(StatesGroup):
    confirm = State()
