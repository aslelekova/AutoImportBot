# car_params_handler.py
import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram import Router, types

from car_analysis import analyze_car_data_auto_ru, process_item_encar_com
from data_parser import parse_auto_ru, parse_encar_com
from file_handler import load_data_from_json, save_to_file
from keyboards import marks_keyboard as KB_brand
from keyboards import models_keyboard as KB_model
from keyboards import year_bounds_keyboard as KB_year
from keyboards import fuel_type_keyboard as KB_fuel
from keyboards import mileage_keyboard as KB_mileage
from keyboards.fuel_type_keyboard import fuel_type_choose
from keyboards.mileage_keyboard import mileage_choose
from keyboards.models_keyboard import model_choose
from keyboards.year_bounds_keyboard import age_choose

router = Router()

logging.basicConfig(filename='bot.log', level=logging.INFO)
logger = logging.getLogger(__name__)


@router.callback_query(KB_brand.BrandChoose.filter(F.action == 'brand_car'))
async def get_brand(call: types.CallbackQuery, callback_data: KB_brand.BrandChoose, state: FSMContext):
    """
    Callback function to handle brand selection.

    :param call: The callback query.
    :param callback_data: The callback data containing selected brand information.
    :param state: The FSM context.
    """
    user_id = call.from_user.id
    try:
        await state.update_data(brand_auto_ru=callback_data.brand_auto_ru)
        await state.update_data(brand_encar_com=callback_data.brand_encar_com)
        await call.message.delete()
        await call.message.answer(
            '🚘 Какая модель вас интересует?',
            reply_markup=model_choose(callback_data.brand_auto_ru)
        )

        logger.info(f"User {user_id} selected brand: {callback_data.brand_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_brand for user {user_id}: {e}")
        await call.message.answer("Произошла ошибка при выборе марки автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_model.ModelChoose.filter(F.action == 'model_car'))
async def get_model(call: types.CallbackQuery, callback_data: KB_model.ModelChoose, state: FSMContext):
    """
    Callback function to handle model selection.

    :param call: The callback query.
    :param callback_data: The callback data containing selected model information.
    :param state: The FSM context.
    """
    user_id = call.from_user.id
    try:
        await state.update_data(model_auto_ru=callback_data.model_auto_ru)
        await state.update_data(model_encar_com=callback_data.model_encar_com)
        await call.message.delete()
        await call.message.answer(
            '🚘 Возраст автомобиля?',
            reply_markup=age_choose()
        )

        logger.info(f"User {user_id} selected model: {callback_data.model_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_model for user {user_id}: {e}")
        await call.message.answer("Произошла ошибка при выборе модели автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_year.YearChoose.filter(F.action == 'year'))
async def get_age(call: types.CallbackQuery, callback_data: KB_year.YearChoose, state: FSMContext):
    """
    Callback function to handle the selection of car age.

    :param call: The callback query.
    :param callback_data: The callback data containing selected age information.
    :param state: The FSM context.
    """
    user_id = call.from_user.id
    try:
        await state.update_data(year_left_bound=callback_data.year_left_bound)
        await state.update_data(year_right_bound=callback_data.year_right_bound)
        await call.message.delete()
        await call.message.answer(
            '🚘 Тип топлива?',
            reply_markup=fuel_type_choose()
        )

        logger.info(
            f"User {user_id} selected year range: {callback_data.year_left_bound}-{callback_data.year_right_bound}")

    except Exception as e:
        logger.error(f"Error in get_age for user {user_id}: {e}")
        await call.message.answer("Произошла ошибка при выборе возраста автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_fuel.FuelChoose.filter(F.action == 'fuel_type'))
async def get_fuel_type(call: types.CallbackQuery, callback_data: KB_fuel.FuelChoose, state: FSMContext):
    """
    Callback function to handle the selection of fuel type.

    :param call: The callback query.
    :param callback_data: The callback data containing selected fuel type information.
    :param state: The FSM context.
    """
    user_id = call.from_user.id
    try:
        await state.update_data(fuel_type_auto_ru=callback_data.fuel_type_auto_ru)
        await state.update_data(fuel_type_encar_com=callback_data.fuel_type_encar_com)
        await call.message.delete()
        await call.message.answer(
            '🚘 Пробег автомобиля?',
            reply_markup=mileage_choose()
        )

        logger.info(f"User {user_id} selected fuel type: {callback_data.fuel_type_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_fuel_type for user {user_id}: {e}")
        await call.message.answer("Произошла ошибка при выборе типа двигателя. Попробуйте еще раз.")


@router.callback_query(KB_mileage.MileageChoose.filter(F.action == 'mileage_bounds'))
async def get_mileage(call: types.CallbackQuery, callback_data: KB_mileage.MileageChoose, state: FSMContext):
    """
    Callback function to handle the selection of mileage bounds.

    :param call: The callback query.
    :param callback_data: The callback data containing selected mileage bounds.
    :param state: The FSM context.
    """
    user_id = call.from_user.id
    try:
        await state.update_data(mileage_left_bound=callback_data.mileage_left_bound)
        await state.update_data(mileage_right_bound=callback_data.mileage_right_bound)
        await call.message.delete()
        await send_car_listings(call.message, state)

        logger.info(
            f"User {user_id} selected mileage bounds: {callback_data.mileage_left_bound}-{callback_data.mileage_right_bound}")

    except Exception as e:
        logger.error(f"Error in get_mileage for user {user_id}: {e}")
        await call.message.answer("Произошла ошибка при загрузке автомобилей. Попробуйте еще раз.")


async def send_car_listings(message: types.Message, state: FSMContext):
    """

    :param message:
    :param state:
    :return:
    """
    user_id = message.from_user.id

    # Retrieve data from the FSM context.
    fsm_data = await state.get_data()
    brand_auto_ru = fsm_data.get('brand_auto_ru')
    brand_encar_com = fsm_data.get('brand_encar_com')
    model_auto_ru = fsm_data.get('model_auto_ru')
    model_encar_com = fsm_data.get('model_encar_com')
    year_left_bound = fsm_data.get('year_left_bound')
    year_right_bound = fsm_data.get('year_right_bound')
    fuel_type_auto_ru = fsm_data.get('fuel_type_auto_ru')
    fuel_type_encar_com = fsm_data.get('fuel_type_encar_com')
    mileage_left_bound = fsm_data.get('mileage_left_bound')
    mileage_right_bound = fsm_data.get('mileage_right_bound')

    if fuel_type_auto_ru == '':
       print_fuel = 'не выбрано'
    else:
        print_fuel = fuel_type_auto_ru.title()
    if year_left_bound == 0 and year_right_bound == 0:
        print_year = 'не выбрано'
    else:
        print_year = f"{year_left_bound} - {year_right_bound}"
    if mileage_left_bound == 0 and mileage_right_bound == 0:
        print_mileage = 'не выбрано'
    else:
        print_mileage = f"{mileage_left_bound} - {mileage_right_bound}"

    await message.answer(
        f"✅Выбранные параметры:\n\n{hbold('Марка: ')}{brand_auto_ru}\n{hbold('Модель: ')}{model_auto_ru}\n"
        f"{hbold('Возраст: ')}{print_year}\n{hbold('Тип топлива: ')}{print_fuel}\n{hbold('Пробег: ')}{print_mileage}")

    await message.answer('Пожалуйста, подождите\nИщем лучшие предложения...')

    # Parse car data from auto.ru and encar.com.
    offers_data_auto_ru = parse_auto_ru(brand_auto_ru, model_auto_ru, year_left_bound, year_right_bound,
                                        fuel_type_auto_ru, mileage_left_bound, mileage_right_bound)
    offers_data_encar_com = parse_encar_com(brand_encar_com, model_encar_com, year_left_bound, year_right_bound,
                                            fuel_type_encar_com, mileage_left_bound, mileage_right_bound)

    # Save parsed data to JSON files.
    save_to_file(offers_data_auto_ru, "data_auto_ru.json")
    save_to_file(offers_data_encar_com, "data_encar_com.json")

    logger.info(f"User {user_id} data saved to files: data_auto_ru.json, data_encar_com.json")

    # Load data from encar.com JSON file.
    data_encar_com = load_data_from_json("data_encar_com.json")

    if not data_encar_com:
        logger.warning(f"User {user_id}: No data found in data_encar_com.json. Restarting car selection process.")
        await restart_car_selection(message, state)
        return

    # Load data from auto.ru JSON file.
    data_auto_ru = load_data_from_json("data_auto_ru.json")
    encoded_data_auto_ru = analyze_car_data_auto_ru(
        data_auto_ru)

    count = 0
    remaining_cards = []
    first_five_cards = []
    for page_data in data_encar_com:
        for item in page_data.get("SearchResults", []):
            if count >= 5:
                break

            card = process_item_encar_com(item, brand_auto_ru, model_auto_ru, encoded_data_auto_ru)
            if card is not None:
                first_five_cards.append(card)
                count += 1

    for i in range(len(first_five_cards) - 1):
        await message.answer(first_five_cards[i])

    if len(first_five_cards) > 4:
        await message.answer(first_five_cards[-1], reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Показать еще", callback_data="show_more_encar_com")]
        ]))
    else:
        await message.answer(first_five_cards[-1])

    for page_data in data_encar_com:
        for item in page_data.get("SearchResults", []):
            card = process_item_encar_com(item, brand_auto_ru, model_auto_ru, encoded_data_auto_ru)
            if card is not None and card not in first_five_cards:
                remaining_cards.append(card)
    await state.update_data(remaining_cards=remaining_cards)


# TODO: change algorithm remaining_cards


@router.callback_query(F.data == 'show_more_encar_com')
async def show_more_callback(call: types.CallbackQuery, state: FSMContext):
    """
    Handler for the "Show More" button in Encar car listings.

    :param call: The CallbackQuery object representing the incoming request.
    :param state: The Finite State Machine context object.

    :return: None
    """
    fsm_data = await state.get_data()
    remaining_cards = fsm_data.get('remaining_cards', [])
    current_index = fsm_data.get('current_index', 0)

    # Calculate the range for the next batch of cards
    next_batch = remaining_cards[current_index:current_index + 5]

    # Display each card in the current batch
    for i, card in enumerate(next_batch):
        if i == len(next_batch) - 1 and current_index + 5 < len(remaining_cards):
            # Add the "Show More" button under the last card of the current batch if there are more cards
            await call.message.answer(
                card,
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="Показать еще", callback_data="show_more_encar_com")]
                    ]
                )
            )
        else:
            await call.message.answer(card)

    # Update the current index
    current_index += 5
    await state.update_data(current_index=current_index)

    await call.answer()


async def restart_car_selection(message: types.Message, state: FSMContext):
    """
    Function to restart the car selection process by asking the user to choose a brand.
    :param message: The message to which the response will be sent.
    :param state: The FSM context containing information about the current chat state.
    :return: None
    """
    user_id = message.from_user.id
    await state.clear()
    await message.answer(
        f"{hbold('Таких машин не найдено.')} Выберите другие параметры.\n\n🚘 Какая марка вас интересует?\n",
        reply_markup=KB_brand.brand_choose()
    )


@router.message()
async def handle_random_message(message: types.Message):
    """
    Function handle_random_message is responsible for handling random messages that the bot cannot process. It sends a reply to the user indicating that the message cannot be processed and suggests writing '/help' for more detailed information.

    :param message: The message received by the bot.
    :return: None
    """
    await message.reply("Простите, я не могу обработать это сообщение. Для получения подробной информации напишите "
                        "/help")
