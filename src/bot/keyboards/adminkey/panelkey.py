from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def admin_main_panel_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🧰 Shop-tools", callback_data="shop-tools-panel")],
        [InlineKeyboardButton(text="✉️ Mailing", callback_data="mail-panel")],
        [InlineKeyboardButton(text="« Back", callback_data="back-main-menu")],
    ])
