from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def admin_shop_tools_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔖 Category", callback_data="category-tools")],
        [InlineKeyboardButton(text="🏷 Promo", callback_data="promo-tools")],
        [InlineKeyboardButton(text="« Back", callback_data="admin-panel")]
    ])

