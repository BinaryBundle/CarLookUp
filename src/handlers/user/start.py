from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import CommandStart

from src.loader import dp
from src.keyboards import get_request_contact_keyboard
from src.states import ConfirmationAccount


@dp.message_handler(CommandStart())
async def start_command(message: Message):
    # TODO Проверка пользователя
    keyboard = get_request_contact_keyboard()
    await ConfirmationAccount.confirm.set()
    await message.answer(
        '<b>Для доступа к функциям бота необходимо пройти регистрацию.</b>',
        reply_markup=keyboard
    )


@dp.message_handler(content_types=ContentType.CONTACT, state=ConfirmationAccount.confirm)
async def confirm_account(message: Message, state: FSMContext):
    if message.contact.user_id == message.from_user.id:
        # TODO Добавление нового пользователя
        await state.finish()
        await message.answer('''<i>Регистрация прошла успешно</i>''', reply_markup=ReplyKeyboardRemove())
    else:
        # TODO Обработка попытки обмануть
        await message.answer('Блокировка аккаунта на 7 дней!')


