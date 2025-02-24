import logging
import sys

from colorama import init, Fore, Back

from aiogram import Dispatcher

from .configs import *
from .handlers import *

init(autoreset=True)

dp = Dispatcher()
setup = BotConfig()


async def bot_run() -> None:
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await handler_manager(dp)
        await setup.bot.delete_webhook(drop_pending_updates=True)
        print(f'{Fore.GREEN}[+] {Fore.WHITE}Bot started')
        await dp.start_polling(setup.bot)
    except AttributeError:
        pass

__all__ = [
    'bot_run',
    'Fore',
    'Back'
]
