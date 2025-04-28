from aiogram import Dispatcher

from .start import router as user_start
from .profile import router as user_profile
from .backer import router as user_backer


async def user_handler(dp: Dispatcher) -> None:
    return dp.include_routers(
        user_start,
        user_profile,
        user_backer
    )


__all__ = [
    'user_handler',
]
