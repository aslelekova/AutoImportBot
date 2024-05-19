# car_params_handler.py
import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold
from magic_filter import F
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
    try:
        await state.update_data(brand_auto_ru=callback_data.brand_auto_ru)
        await state.update_data(brand_encar_com=callback_data.brand_encar_com)
        await call.message.edit_text(f'🚘 Какая марка вас интересует?\n\n✅ Ответ: {callback_data.answer}')
        await call.message.answer(
            '🚘 Какая модель вас интересует?',
            reply_markup=model_choose(callback_data.brand_auto_ru)
        )

        logger.info(f"Brand selected: {callback_data.brand_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_brand: {e}")
        await call.message.answer("Произошла ошибка при выборе марки автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_model.ModelChoose.filter(F.action == 'model_car'))
async def get_model(call: types.CallbackQuery, callback_data: KB_model.ModelChoose, state: FSMContext):
    """
    Callback function to handle model selection.

    :param call: The callback query.
    :param callback_data: The callback data containing selected model information.
    :param state: The FSM context.
    """
    try:
        await state.update_data(model_auto_ru=callback_data.model_auto_ru)
        await state.update_data(model_encar_com=callback_data.model_encar_com)
        await call.message.edit_text(f'🚘 Какая модель вас интересует?\n\n✅ Ответ: {callback_data.answer}')
        await call.message.answer(
            '🚘 Возраст автомобиля?',
            reply_markup=age_choose()
        )

        logger.info(f"Model selected: {callback_data.model_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_model: {e}")
        await call.message.answer("Произошла ошибка при выборе модели автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_year.YearChoose.filter(F.action == 'year'))
async def get_age(call: types.CallbackQuery, callback_data: KB_year.YearChoose, state: FSMContext):
    """
    Callback function to handle the selection of car age.

    :param call: The callback query.
    :param callback_data: The callback data containing selected age information.
    :param state: The FSM context.
    """
    try:
        await state.update_data(year_left_bound=callback_data.year_left_bound)
        await state.update_data(year_right_bound=callback_data.year_right_bound)
        await call.message.edit_text(f'🚘 Возраст автомобиля?\n\n✅ Ответ: {callback_data.answer}')
        await call.message.answer(
            '🚘 Тип двигателя?',
            reply_markup=fuel_type_choose()
        )

        logger.info(f"Year range selected: {callback_data.year_left_bound}-{callback_data.year_right_bound}")

    except Exception as e:
        logger.error(f"Error in get_age: {e}")
        await call.message.answer("Произошла ошибка при выборе возраста автомобиля. Попробуйте еще раз.")


@router.callback_query(KB_fuel.FuelChoose.filter(F.action == 'fuel_type'))
async def get_fuel_type(call: types.CallbackQuery, callback_data: KB_fuel.FuelChoose, state: FSMContext):
    """
    Callback function to handle the selection of fuel type.

    :param call: The callback query.
    :param callback_data: The callback data containing selected fuel type information.
    :param state: The FSM context.
    """
    try:
        await state.update_data(fuel_type_auto_ru=callback_data.fuel_type_auto_ru)
        await state.update_data(fuel_type_encar_com=callback_data.fuel_type_encar_com)
        await call.message.edit_text(f'🚘 Тип двигателя?\n\n✅ Ответ: {callback_data.answer}')
        await call.message.answer(
            '🚘 Пробег автомобиля?',
            reply_markup=mileage_choose()
        )

        logger.info(f"Fuel type selected: {callback_data.fuel_type_auto_ru}")

    except Exception as e:
        logger.error(f"Error in get_fuel_type: {e}")
        await call.message.answer("Произошла ошибка при выборе типа двигателя. Попробуйте еще раз.")


@router.callback_query(KB_mileage.MileageChoose.filter(F.action == 'mileage_bounds'))
async def get_mileage(call: types.CallbackQuery, callback_data: KB_mileage.MileageChoose, state: FSMContext):
    """
    Callback function to handle the selection of mileage bounds.

    :param call: The callback query.
    :param callback_data: The callback data containing selected mileage bounds.
    :param state: The FSM context.
    """

    await state.update_data(mileage_left_bound=callback_data.mileage_left_bound)
    await state.update_data(mileage_right_bound=callback_data.mileage_right_bound)
    await call.message.edit_text(f'🚘 Пробег автомобиля?\n\n✅ Ответ: {callback_data.answer}')
    await send_car_listings(call.message, state)

    logger.info(f"Mileage bounds selected: {callback_data.mileage_left_bound}-{callback_data.mileage_right_bound}")


async def send_car_listings(message: types.Message, state: FSMContext):
    await message.answer('Please, waiting...')

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

    # Parse car data from auto.ru and encar.com.
    offers_data_auto_ru = parse_auto_ru(brand_auto_ru, model_auto_ru, year_left_bound, year_right_bound,
                                        fuel_type_auto_ru, mileage_left_bound, mileage_right_bound)
    offers_data_encar_com = parse_encar_com(brand_encar_com, model_encar_com, year_left_bound, year_right_bound,
                                            fuel_type_encar_com, mileage_left_bound, mileage_right_bound)

    # Save parsed data to JSON files.
    save_to_file(offers_data_auto_ru, "data_auto_ru.json")
    save_to_file(offers_data_encar_com, "data_encar_com.json")

    logger.info("Data saved to files: data_auto_ru.json, data_encar_com.json")

    # Load data from encar.com JSON file.
    data_encar_com = load_data_from_json("data_encar_com.json")

    if not data_encar_com:
        logger.warning("No data found in data_encar_com.json. Restarting car selection process.")
        await restart_car_selection(message, state)
        return

    # Load data from auto.ru JSON file.
    data_auto_ru = load_data_from_json("data_auto_ru.json")
    brand, model, encoded_data_auto_ru = analyze_car_data_auto_ru(
        data_auto_ru)

    count = 0
    for page_data in data_encar_com:
        for item in page_data.get("SearchResults", []):
            if count >= 5:
                break

            card = process_item_encar_com(item, brand, model, encoded_data_auto_ru)
            if card is not None:
                await message.answer(card)
                count += 1

            if count >= 5:
                await message.answer("Show More", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="Show More", callback_data="show_more_encar_com")]
                ]))
                break


async def restart_car_selection(message: types.Message, state: FSMContext):
    """
    Function to restart the car selection process by asking the user to choose a brand.
    :param message: The message to which the response will be sent.
    :param state: The FSM context containing information about the current chat state.
    :return: None
    """

    await state.clear()
    await message.answer(
        f"{hbold('Таких машин не найдено.')} Выберите другие параметры.\n\n🚘 Какая марка вас интересует?'\n",
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
