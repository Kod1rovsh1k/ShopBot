from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)


def user_profile_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏷 Promo", callback_data="promo"),
         InlineKeyboardButton(text="👥 Referral", callback_data="referral")],
        [InlineKeyboardButton(text="📜 Product-list", callback_data="product-list")],
        [InlineKeyboardButton(text="💳 Add-balance", callback_data="add-balance")],
        [InlineKeyboardButton(text="« Back", callback_data="back-main-menu")],
    ])
