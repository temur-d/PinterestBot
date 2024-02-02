from aiogram import Dispatcher

from .commands import register_commands_handler
from .callback_query_handlers import register_callback_query_handlers

def register_user_handlers(dp: Dispatcher) -> None:
    register_commands_handler(dp)
    register_callback_query_handlers(dp)
    