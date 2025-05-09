from aiogram import Router, F, types
from aiogram.methods import EditMessageText, SendMessage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from ...keyboards import *

router = Router()


class MailingState(StatesGroup):
    text = State()
    photo = State()


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
