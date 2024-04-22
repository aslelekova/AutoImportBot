# start_handler.py
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from magic_filter import F
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards import marks_keyboard as KB
from data_parser import parse_auto_ru, parse_encar_com
from file_handler import save_to_file, load_data_from_json
from car_analysis import analyze_car_data_auto_ru, analyze_car_data_encar_com
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


