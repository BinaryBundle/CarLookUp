from aiogram.types import Message

from src.loader import dp


# Эхо для дебага
@dp.message_handler(content_types=['*'])
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')
