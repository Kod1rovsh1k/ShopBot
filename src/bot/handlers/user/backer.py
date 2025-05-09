from aiogram import Router, F, types
from aiogram.methods import EditMessageText

from aiogram.fsm.context import FSMContext

from ...keyboards import *

router = Router()


@router.callback_query(F.data == "back-main-menu")
async def cmd_back_main_menu(call: types.CallbackQuery, state: FSMContext) -> EditMessageText:
    await state.set_state(None)
    return call.message.edit_text(
        f'Hello',
        reply_markup=user_main_menu_ikb(call.from_user.id)
    )
