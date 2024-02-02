from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .database_session import DBMiddleware

def register_middlewares(dp: Dispatcher, pool: sessionmaker) -> None:
    dp.setup_middleware(DBMiddleware(pool))