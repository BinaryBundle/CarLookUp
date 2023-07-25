from aiogram.types import Message
from aiogram.types import ContentType

from src.loader import dp


# Заглушка для обрабоки пикч
@dp.message_handler(content_types=ContentType.PHOTO)
async def get_car_photo(message: Message):
    await message.answer('Мне удалось распознать, это машина. Вот её гос номер <code>М228АХ18</code>')
