from aiogram import Router, types
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text="Hello")


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="I can help you to find a car.")
