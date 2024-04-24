from datetime import datetime

from aiogram import types

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class YearChoose(CallbackData, prefix='y'):
    action: str
    year_left_bound: str
    year_right_bound: str
    answer: str


def age_choose():
    current_year = datetime.now().year
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(text="до 3 лет", callback_data=YearChoose(action='year',
                                                                               answer='до 3 лет',
                                                                               year_left_bound=str(current_year - 3),
                                                                               year_right_bound=str(current_year)).pack()),
        types.InlineKeyboardButton(text="от 3 до 5 лет", callback_data=YearChoose(action='year',
                                                                                    answer='от 3 до 5 лет',
                                                                                    year_left_bound=str(current_year - 5),
                                                                                    year_right_bound=str(current_year - 3)).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='от 5 до 7 лет', callback_data=YearChoose(action='year',
                                                                                    answer='от 5 до 7 лет',
                                                                                    year_left_bound=str(current_year - 7),
                                                                                    year_right_bound=str(current_year - 5)).pack()),
        types.InlineKeyboardButton(text="старше 7 лет", callback_data=YearChoose(action='year',
                                                                                   answer='старше 7 лет',
                                                                                   year_left_bound="1990",
                                                                                   year_right_bound=str(current_year - 7)).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text='Пропустить', callback_data=YearChoose(action='year',
                                                                                    answer='Пропустить',
                                                                                 year_left_bound='',
                                                                                 year_right_bound='').pack())
    )
    return kb.as_markup()
