from aiogram import executor

from handlers import dp


async def on_startup():
    pass


async def on_shutdown():
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
