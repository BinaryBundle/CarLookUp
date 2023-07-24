from aiogram.types import Message

from src.loader import dp


@dp.message_handler()
async def echo(message: Message):
    await message.answer('Ajaja')
