from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import get_user, add_user, get_lang_user

from keyboards import lang_buttons

async def start_command_handler(message: Message, session: AsyncSession, state: FSMContext) -> None:
    
    if not await get_user(session, message.from_user.id):
        await add_user(
            session=session,
            chat_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )

    lang_user = await get_lang_user(session, message.from_user.id)

    if lang_user is None:

        await message.answer(
            text='🇷🇺 Выберите язык\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Choose language\n🇺🇿 Tilni tanlang',
            reply_markup=lang_buttons
        )
    else:
        text = {
            'ru': 'Привет! С помощью этого бота вы сможете скачивать видео с <b>Pinterest</b>',
            'en': 'Hello! With the help of this bot, you can download videos from <b>Pinterest</b>. To download, send the video link.',
            'uz': 'Salom! Bu bot orqali Siz <b>Pinterest</b>-dan videoni yuklab olishingiz mumkin. Yuklash uchun, video havolasini yuboring.'
        }

        await message.answer(text=text[lang_user])

    await state.finish()

async def lang_command_handler(message: Message, session: AsyncSession, state: FSMContext) -> None:

    if not await get_user(session, message.from_user.id):
        await add_user(
            session=session,
            chat_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )

    await message.answer(
        text='🇷🇺 Выберите язык\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Choose language\n🇺🇿 Tilni tanlang',
        reply_markup=lang_buttons
    )

    await state.finish()

def register_commands_handler(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start_command_handler,
        commands=['start'],
        state='*'
    )
    dp.register_message_handler(
        lang_command_handler,
        commands=['lang'],
        state='*'
    )