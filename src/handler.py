from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from base_func import router, Go, get_forms
from keyboards.base_kb import go_back
from bot_settings import settings


@router.callback_query(F.data == "stop")
async def command_back(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text="Stop")
    await state.clear()


@router.callback_query(F.data == "forms")
async def forms(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_caption(
        caption="Press stop\nor push menu -> command /stop",
        reply_markup=go_back(size=1),
    )
