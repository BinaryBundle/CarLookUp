from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def to_build_keyboard(*args, **kwargs) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(**kwargs)
    for button_data in args:
        keyboard.insert(KeyboardButton(**button_data))
    return keyboard
