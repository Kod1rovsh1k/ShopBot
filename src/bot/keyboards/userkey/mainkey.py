from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)
import os

def user_agreement() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Agree", callback_data='agree')],
    ])

def user_main_menu_ikb(chat_id: int) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎀 Shop", callback_data="shop")],
        [InlineKeyboardButton(text="👤 Profile", callback_data="profile")],
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")],
    ])

    if chat_id in [int(os.getenv('CHAT_ID'))]:
        ikb.inline_keyboard.append([InlineKeyboardButton(text="🎈 Admin", callback_data="admin")])

    return ikb
