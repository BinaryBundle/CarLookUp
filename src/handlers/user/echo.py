from aiogram.types import Message
from aiogram.types import ContentType

from src.loader import dp

# Эхо для дебага
@dp.message_handler(content_types=ContentType.TEXT)
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')
