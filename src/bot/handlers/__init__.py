from aiogram import Dispatcher

from .user import user_handler
from .admin import admin_handler


async def handler_manager(dp: Dispatcher) -> None:
    await user_handler(dp)
    await admin_handler(dp)


__all__ = [
    'handler_manager',
]
