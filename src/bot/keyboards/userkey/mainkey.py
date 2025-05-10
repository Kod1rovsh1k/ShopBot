import os

from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)


def user_main_menu_ikb(chat_id: int) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎀 Shop", callback_data="shop")],
        [InlineKeyboardButton(text="👤 Profile", callback_data="profile")],
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")],
    ])

    if chat_id in [int(os.getenv('CHAT_ID'))]:
        ikb.inline_keyboard.append([InlineKeyboardButton(text="🎈 Admin", callback_data="admin-panel")])

    return ikb
