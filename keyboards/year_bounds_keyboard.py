# year_bounds_keyboard.py
from datetime import datetime

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class YearChoose(CallbackData, prefix='y'):
    action: str
    year_left_bound: int
    year_right_bound: int
    answer: str


def age_choose():
    """
    Generates an inline keyboard for choosing car age ranges.

    :return: InlineKeyboardMarkup: Inline keyboard with car age range options.
    """
    current_year = datetime.now().year
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(text="до 3 лет", callback_data=YearChoose(action='year',
                                                                             answer='до 3 лет',
                                                                             year_left_bound=(current_year - 3),
                                                                             year_right_bound=
                                                                             current_year).pack()),
        types.InlineKeyboardButton(text="от 3 до 5 лет", callback_data=YearChoose(action='year',
                                                                                  answer='от 3 до 5 лет',
                                                                                  year_left_bound=(current_year - 5),
                                                                                  year_right_bound=(
                                                                                      current_year - 3)).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='от 5 до 7 лет', callback_data=YearChoose(action='year',
                                                                                  answer='от 5 до 7 лет',
                                                                                  year_left_bound=(current_year - 7),
                                                                                  year_right_bound=(
                                                                                      current_year - 5)).pack()),
        types.InlineKeyboardButton(text="старше 7 лет", callback_data=YearChoose(action='year',
                                                                                 answer='старше 7 лет',
                                                                                 year_left_bound=1990,
                                                                                 year_right_bound=(
                                                                                     current_year - 7)).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='Пропустить', callback_data=YearChoose(action='year',
                                                                               answer='Пропустить',
                                                                               year_left_bound=0,
                                                                               year_right_bound=0).pack())
    )
    return kb.as_markup()
