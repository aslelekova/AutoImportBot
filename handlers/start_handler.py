# start_handler.py
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards.marks_keyboard import brand_choose

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f'✋ Приветствую, {message.from_user.username}!'
                         f'\n\nЯ Telegram-бот для расчета стоимости корейских автомобилей, я помогу '
                         f'рассчитать цену и другие детали по доставке машины в РФ.\n\n'
                         f'💰 Так же я предоставлю информацию по похожим автомобилям в России для сравнения.\n\n🚘 '
                         f'Какая марка вас интересует?', reply_markup=brand_choose())


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="I can help you to find a car.")
