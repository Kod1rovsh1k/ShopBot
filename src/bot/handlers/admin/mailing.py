from typing import Any, Coroutine

from aiogram import Router, F, types
from aiogram.methods import EditMessageText, SendMessage, SendPhoto
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from ...keyboards import *
from ...database import *

router = Router()
user_query = UserQuery()


class MailingState(StatesGroup):
    text = State()
    img = State()


@router.callback_query(F.data == "mail-panel")
async def cmd_admin_mailing(call: types.CallbackQuery, state: FSMContext) -> EditMessageText:
    await state.set_state(MailingState.text)
    return call.message.edit_text(
        f'📨 <b>Input text, for mailing:</b>',
        reply_markup=admin_mailing_panel_ikb(),
    )


@router.message(MailingState.text)
async def cmd_state_text(msg: types.Message, state: FSMContext) -> SendMessage:
    await state.update_data(text=msg.text)
    await state.set_state(None)
    data = await state.get_data()
    return msg.answer(
        f'📮 <b>Mailing menu:</b>\n'
        f'➖➖➖➖➖➖➖➖➖➖\n'
        f'📄 <b>Text:</b> <blockquote>{data.get("text")}</blockquote>\n',
        reply_markup=admin_mailing_choice_ikb(),
    )


@router.callback_query(F.data == "add-picture")
async def cmd_state_img(call: types.CallbackQuery, state: FSMContext) -> SendMessage:
    await state.set_state(MailingState.img)
    return call.message.answer(
        f'Send img'
    )


@router.message(MailingState.img, F.content_type.in_(['photo']))
async def cmd_state_photo(msg: types.Message, state: FSMContext) -> SendPhoto:
    if msg.photo:
        await state.update_data(img=msg.photo[-1].file_id)

    await state.set_state(None)
    data = await state.get_data()

    return msg.answer_photo(
        photo=data.get("img"),
        caption=f'📮 <b>Mailing menu:</b>\n'
                f'➖➖➖➖➖➖➖➖➖➖\n'
                f'📄 <b>Text:</b> <blockquote>{data.get("text")}</blockquote>\n',
        reply_markup=admin_mailing_choice_ikb(),
    )


@router.callback_query(F.data == "send-mailing")
async def cmd_send_mailing(call: types.CallbackQuery, state: FSMContext) -> types.CallbackQuery:
    data = await state.get_data()

    text_mailing = data.get('text')
    img_mailing = data.get('img')

    await user_query.userMailing(text_mailing, img_mailing, sender_chat_id=call.from_user.id)
    await call.answer("✅ Mail send")

    if img_mailing:
        await call.message.delete()
        await call.message.answer(
            f"<b>Admin-panel</b>",
            reply_markup=admin_main_panel_ikb()
        )
    else:
        await call.message.edit_text(
            "<b>Admin-panel</b>",
            reply_markup=admin_main_panel_ikb()
        )

    await state.set_state(None)
    return call
