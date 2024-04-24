# car_params_handler.py
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from magic_filter import F
from aiogram import Router, types
from aiogram.filters import Command

from car_analysis import analyze_car_data_encar_com, analyze_car_data_auto_ru
from data_parser import parse_auto_ru, parse_encar_com
from file_handler import save_to_file, load_data_from_json
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


@router.callback_query(KB_brand.BrandChoose.filter(F.action == 'brand_car'))
async def get_brand(call: types.CallbackQuery, callback_data: KB_brand.BrandChoose, state: FSMContext):
    await state.update_data(brand_auto_ru=callback_data.brand_auto_ru)
    await state.update_data(brand_encar_com=callback_data.brand_encar_com)
    await call.message.edit_text(f'🚘 Какая марка вас интересует?\n\n✅ Ответ: {callback_data.answer}')
    await call.message.answer(
        '🚘 Какая модель вас интересует?',
        reply_markup=model_choose(callback_data.brand_auto_ru)
    )


@router.callback_query(KB_model.ModelChoose.filter(F.action == 'model_car'))
async def get_model(call: types.CallbackQuery, callback_data: KB_model.ModelChoose, state: FSMContext):
    await state.update_data(model_auto_ru=callback_data.model_auto_ru)
    await state.update_data(model_encar_com=callback_data.model_encar_com)
    await call.message.edit_text(f'🚘 Какая модель вас интересует?\n\n✅ Ответ: {callback_data.answer}')
    await call.message.answer(
        '🚗 Возраст автомобиля?',
        reply_markup=age_choose()
    )


@router.callback_query(KB_year.YearChoose.filter(F.action == 'year'))
async def get_age(call: types.CallbackQuery, callback_data: KB_year.YearChoose, state: FSMContext):
    await state.update_data(year_left_bound=callback_data.year_left_bound)
    await state.update_data(year_right_bound=callback_data.year_right_bound)
    await call.message.edit_text(f'🚗 Возраст автомобиля?\n\n✅ Ответ: {callback_data.answer}')
    await call.message.answer(
        '🚗 Тип двигателя?',
        reply_markup=fuel_type_choose()
    )


@router.callback_query(KB_fuel.FuelChoose.filter(F.action == 'fuel_type'))
async def get_fuel_type(call: types.CallbackQuery, callback_data: KB_fuel.FuelChoose, state: FSMContext):
    await state.update_data(fuel_type_auto_ru=callback_data.fuel_type_auto_ru)
    await state.update_data(fuel_type_encar_com=callback_data.fuel_type_encar_com)
    await call.message.edit_text(f'🚗 Тип двигателя?\n\n✅ Ответ: {callback_data.answer}')
    await call.message.answer(
        '🚗 Пробег автомобиля?',
        reply_markup=mileage_choose()
    )


@router.callback_query(KB_mileage.MileageChoose.filter(F.action == 'mileage_bounds'))
async def get_mileage(call: types.CallbackQuery, callback_data: KB_mileage.MileageChoose, state: FSMContext):
    await state.update_data(mileage_left_bound=callback_data.mileage_left_bound)
    await state.update_data(mileage_right_bound=callback_data.mileage_right_bound)
    await call.message.edit_text(f'🚗 Пробег автомобиля?\n\n✅ Ответ: {callback_data.answer}')


@router.message(Command("cars"))
async def handle_help(message: types.Message, state: FSMContext):
    # Get brand from the FSM context
    fsm_data = await state.get_data()
    brand_auto_ru = fsm_data.get('brand_auto_ru')
    brand_encar_com = fsm_data.get('brand_encar_com')
    model_auto_ru = fsm_data.get('model_auto_ru')
    model_encar_com = fsm_data.get('model_encar_com')
    year_left_bound = fsm_data.get('year_left_bound')
    year_right_bound = fsm_data.get('year_right_bound')
    fuel_type_auto_ru = fsm_data.get('fuel_type_auto_ru')
    fuel_type_encar_com = fsm_data.get('fuel_type_encar_com')
    mileage_left_bound  = fsm_data.get('mileage_left_bound')
    mileage_right_bound  = fsm_data.get('mileage_right_bound')

    print(fsm_data)
    # offers_data_auto_ru = parse_auto_ru(brand_auto_ru, model_auto_ru, year_left_bound, year_right_bound, fuel_type_auto_ru)
    # offers_data_encar_com = parse_encar_com(brand_encar_com, model_encar_com, year_left_bound, year_right_bound, fuel_type_encar_com)
    #
    # # Saving the parsed data to a file.
    # save_to_file(offers_data_auto_ru, "data_auto_ru.json")
    # save_to_file(offers_data_encar_com, "data_encar_com.json")
    #
    # data_auto_ru = load_data_from_json("data_auto_ru.json")
    # brand, model, formatted_average_price, links_auto_ru = analyze_car_data_auto_ru(
    #     data_auto_ru)
    #
    # data_encar_com = load_data_from_json("data_encar_com.json")
    #
    # cards = analyze_car_data_encar_com(data_encar_com, brand, model, formatted_average_price, links_auto_ru)
    #
    # for i, card in enumerate(cards, start=1):
    #     await message.answer(card)
