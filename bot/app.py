import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from data import Config
from database import get_engine, BaseModel
from middlerware import register_middlewares
from handlers import register_user_handlers

async def init_models() -> None:
    engine: Engine = get_engine()

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

async def register_all_dependencies(dp: Dispatcher, db_pool: sessionmaker) -> None:
    
    register_middlewares(dp, db_pool)
    register_user_handlers(dp)
    
async def main() -> None:
    
    bot: Bot = Bot(
        token=Config.token,
        parse_mode=ParseMode.HTML
    )
    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(
        bot=bot,
        storage=storage
    )
    engine: Engine = get_engine()
    db_pool = sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    await init_models()
    await register_all_dependencies(dp, db_pool)
    try:
        print('Bot started !')
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        bot_session = await bot.get_session()
        await bot_session.close()
        print('Bot stopped !')

if __name__ == '__main__':
    asyncio.run(main())
