import logging
from aiogram import Bot
from aiogram import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
