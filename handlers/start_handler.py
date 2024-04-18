# start_handler.py
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from magic_filter import F
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.filters.callback_data import CallbackData
from keyboards import marks_keyboard as KB
from data_parser import parse_auto_ru, parse_encar_com
from file_handler import save_to_file, load_data_from_json
from car_analysis import analyze_car_data_auto_ru, analyze_car_data_encar_com
from keyboards.marks_keyboard import brand_choose

router = Router()


class FSMPrice(StatesGroup):
    brand_auto_ru = State()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f'✋ Привет, {message.from_user.username}!'
                         f'\n\nЯ Telegram-бот для расчета стоимости корейских автомобилей, я помогу '
                         f'рассчитать цену и другие детали по доставке машины в РФ.\n\n'
                         f'💰 Так же я предоставлю информацию по похожим автомобилям в России для сравнения.\n\n🚘 '
                         f'Какая марка вас интересует?', reply_markup=brand_choose())


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="I can help you to find a car.")


@router.message(Command("cars"))
async def handle_help(message: types.Message, state: FSMContext):
    # Get brand from the FSM context
    fsm_data = await state.get_data()
    brand_auto_ru = fsm_data.get('brand_auto_ru')
    brand_encar_com = fsm_data.get('brand_encar_com')

    offers_data_auto_ru = parse_auto_ru(brand_auto_ru)

    offers_data_encar_com = parse_encar_com(brand_encar_com)

    # Saving the parsed data to a file.
    save_to_file(offers_data_auto_ru, "data_auto_ru.json")
    save_to_file(offers_data_encar_com, "data_encar_com.json")

    data_auto_ru = load_data_from_json("data_auto_ru.json")

    brand, model, formatted_average_price, links_auto_ru = analyze_car_data_auto_ru(
        data_auto_ru)

    data_encar_com = load_data_from_json("data_encar_com.json")

    cards = analyze_car_data_encar_com(data_encar_com, brand, model, formatted_average_price, links_auto_ru)

    for i, card in enumerate(cards, start=1):
        await message.answer(card)


@router.callback_query(KB.BrandChoose.filter(F.action == 'brand_car'))
async def get_dvs(call: types.CallbackQuery, callback_data: KB.BrandChoose, state: FSMContext):
    await state.update_data(brand_auto_ru=callback_data.brand_auto_ru)
    await state.update_data(brand_encar_com=callback_data.brand_encar_com)
    # await state.set_state(FSMPrice.dvs)
    # await state.update_data(age_answer=callback_data.answer)
    await call.message.edit_text(f'🚗 Какая марка вас интересует?\n\n✅ Ответ: {callback_data.answer}')
