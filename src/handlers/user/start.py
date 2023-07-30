from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import CommandStart

from src.loader import dp
from src.keyboards import get_request_contact_keyboard
from src.services.users import select_user_by_id, insert_new_user
from src.states import ConfirmationAccount


@dp.message_handler(CommandStart())
async def start_command(message: Message):
    user = await select_user_by_id(message.from_user.id)
    if not user:
        keyboard = get_request_contact_keyboard()
        await ConfirmationAccount.confirm.set()
        await message.answer(
            '<b>Для доступа к функциям бота необходимо пройти регистрацию.</b>',
            reply_markup=keyboard
        )
    else:
        await message.answer(f'С возвращением, {user.name}')


@dp.message_handler(content_types=ContentType.CONTACT, state=ConfirmationAccount.confirm)
async def confirm_account(message: Message, state: FSMContext):
    user = message.from_user
    if message.contact.user_id == message.from_user.id:
        result = await insert_new_user(
            telegram_id=user.id,
            username=user.username,
            name=user.first_name,
            surname=user.last_name,
            phone_number=message.contact.phone_number
        )
        if not result:
            await message.answer('Внутренняя ошибка. Попробуйте выполнить регистрацию позднее')
        else:
            await state.finish()
            await message.answer('''<i>Регистрация прошла успешно</i>''', reply_markup=ReplyKeyboardRemove())
    else:
        # TODO Обработка попытки обмануть
        await message.answer('Блокировка аккаунта на 7 дней!')


