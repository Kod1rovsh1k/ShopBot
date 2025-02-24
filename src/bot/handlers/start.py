from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.reply(
        f'Hello, @{msg.from_user.username}',
    )
