from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import get_user, add_user

async def lang_callback_query_handler(call: CallbackQuery, session: AsyncSession, state: FSMContext) -> None:
    
    if not await get_user(session, call.from_user.id):
        await add_user(
            session=session,
            chat_id=call.from_user.id,
            full_name=call.from_user.full_name,
            username=call.from_user.username
        )

    await state.finish()


def register_callback_query_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(
        lang_callback_query_handler,
        text=Text(['ru', 'en', 'uz']),
        state='*'
    )
