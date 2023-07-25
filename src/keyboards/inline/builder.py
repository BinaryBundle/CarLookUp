
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def to_build_keyboard(*args, **kwargs) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(**kwargs)
    for button_data in args:
        keyboard.insert(InlineKeyboardButton(**button_data))
    return keyboard

