from colorama import init, Fore

from dotenv import load_dotenv
import sys
import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.token import TokenValidationError


class BotConfig:
    init(autoreset=True)
    load_dotenv()

    TOKEN = os.getenv('TOKEN')

    def __init__(self) -> None:
        try:
            if not os.path.isfile(".env"):
                with open(".env", "w") as env:
                    print(f'{Fore.YELLOW}[~] {Fore.WHITE}File ({Fore.GREEN}.env{Fore.WHITE}) was successful created')
                    env.write("TOKEN=YOUR_TOKEN\nCHAT_ID=YOUR_CHAT_ID")
                    env.close()

            self.bot = Bot(token=self.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        except TokenValidationError:
            print(
                f'{Fore.RED}[-] {Fore.WHITE}Token validation error, fill out just now file ({Fore.GREEN}.env{Fore.WHITE})')
