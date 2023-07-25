from aiogram.types import Message
from aiogram.dispatcher.filters import Regexp

from src.loader import dp


# Заглушка для РУ машин
@dp.message_handler(Regexp(r'^[АВЕКМНОРСТУХ]|\d\d{3}[АВЕКМНОРСТУХ]{2}\d{1,3}$'))
async def search_car_by_text(message: Message):
    await message.answer('Поиск...')
