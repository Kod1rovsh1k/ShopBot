from aiogram import Dispatcher

from .panel import router as admin_panel
from .mailing import router as admin_mailing
from .shop_tools import router as admin_shop_tools


async def admin_handler(dp: Dispatcher) -> None:
    return dp.include_routers(
        admin_panel,
        admin_shop_tools,
        admin_mailing,
    )


__all__ = [
    'admin_handler',
]
