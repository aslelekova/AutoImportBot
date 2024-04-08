# handlers.py
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from data_parser import parse_auto_ru
from file_handler import save_to_file, load_data_from_json
from car_analysis import analyze_car_data

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text="Hello!\nWhat mark of car would you like to buy?")


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="I can help you to find a car.")


@router.message(Command("cars"))
async def handle_help(message: types.Message):
    # Parsing data from auto.ru.
    offers_data = parse_auto_ru()

    # Saving the parsed data to a file.
    save_to_file(offers_data, "data_auto_ru.json")

    data = load_data_from_json("data_auto_ru.json")

    # Analyzing car data and sending information to the user.
    for item in data:
        card = analyze_car_data([item])
        await message.answer(card)
