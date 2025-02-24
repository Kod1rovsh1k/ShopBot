from aiogram import Dispatcher

from .start import router as user_start


async def handler_manager(dp: Dispatcher) -> None:
    dp.include_routers(
        user_start,
    )


__all__ = [
    'handler_manager',
]
