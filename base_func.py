from openai import AsyncOpenAI
from aiogram.fsm.state import State, StatesGroup
from bot_settings import settings
from aiogram import Router
from aiogram.fsm.context import FSMContext


router = Router()

gpt_client = AsyncOpenAI(api_key=settings.API_KEY_G)


class Go(StatesGroup):
    go_promt = State()
    dialog = State()


async def get_forms(data: dict):
    return data
