# fuel_type_keyboard.py
from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class FuelChoose(CallbackData, prefix='f'):
    action: str
    fuel_type_auto_ru: str
    fuel_type_encar_com: str
    answer: str


def fuel_type_choose():
    """
    Create an inline keyboard for choosing fuel types.

    :return: Inline keyboard markup for fuel type selection.
    """
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(text="Бензин", callback_data=FuelChoose(action='fuel_type',
                                                                           answer='Бензин',
                                                                           fuel_type_auto_ru='GASOLINE',
                                                                           fuel_type_encar_com='가솔린').pack()),
        types.InlineKeyboardButton(text='Дизель', callback_data=FuelChoose(action='fuel_type',
                                                                           answer='Дизель',
                                                                           fuel_type_auto_ru='DIESEL',
                                                                           fuel_type_encar_com='디젤').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='Электро', callback_data=FuelChoose(action='fuel_type',
                                                                            answer='Электро',
                                                                            fuel_type_auto_ru='ELECTRO',
                                                                            fuel_type_encar_com='전기').pack()),
        types.InlineKeyboardButton(text="Гибрид", callback_data=FuelChoose(action='fuel_type',
                                                                           answer='Гибрид',
                                                                           fuel_type_auto_ru='HYBRID',
                                                                           fuel_type_encar_com='가솔린+전기 디젤+전기').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='Пропустить', callback_data=FuelChoose(action='fuel_type',
                                                                               answer='Пропустить',
                                                                               fuel_type_auto_ru='',
                                                                               fuel_type_encar_com='').pack())
    )
    return kb.as_markup()
