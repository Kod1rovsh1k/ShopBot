from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)


def user_main_menu_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Profile", callback_data="profile")],
        [InlineKeyboardButton(text="🎀 Shop", callback_data="shop"),
         InlineKeyboardButton(text="🖍 Support", callback_data="support")],
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")],
    ])
