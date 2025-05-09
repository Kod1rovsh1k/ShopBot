from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def admin_mailing_panel_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="« Back", callback_data="admin-panel")],
    ])


def admin_mailing_choice_ikb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Add Picture", callback_data="add-picture")],
        [InlineKeyboardButton(text="« Back", callback_data="admin-panel"),
         InlineKeyboardButton(text="Next »", callback_data="send-mailing")],
    ])
