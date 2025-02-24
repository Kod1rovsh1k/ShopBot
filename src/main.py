import asyncio

from bot import *

async def main() -> None:
    await bot_run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"{Fore.RED}[!] {Fore.WHITE}Bot stopped")
