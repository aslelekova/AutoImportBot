# mileage_keyboard.py
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MileageChoose(CallbackData, prefix='m'):
    action: str
    mileage_left_bound: int
    mileage_right_bound: int
    answer: str


def mileage_choose():
    """
    Generates an inline keyboard for choosing mileage bounds.

    :return: InlineKeyboardMarkup: Inline keyboard with mileage options.
    """
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(text="до 10 000 км", callback_data=MileageChoose(action='mileage_bounds',
                                                                                    answer='до 10 000 км',
                                                                                    mileage_left_bound=0,
                                                                                    mileage_right_bound=10000).pack()),
        types.InlineKeyboardButton(text="до 20 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 20 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=20000).pack()),
        types.InlineKeyboardButton(text="до 30 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 30 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=30000).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="до 40 000 км", callback_data=MileageChoose(action='mileage_bounds',
                                                                                    answer='до 40 000 км',
                                                                                    mileage_left_bound=0,
                                                                                    mileage_right_bound=40000).pack()),
        types.InlineKeyboardButton(text="до 50 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 50 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=50000).pack()),
        types.InlineKeyboardButton(text="до 60 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 60 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=60000).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="до 70 000 км", callback_data=MileageChoose(action='mileage_bounds',
                                                                                    answer='до 70 000 км',
                                                                                    mileage_left_bound=0,
                                                                                    mileage_right_bound=70000).pack()),
        types.InlineKeyboardButton(text="до 80 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 80 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=80000).pack()),
        types.InlineKeyboardButton(text="до 100 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 100 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=100000).pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="до 120 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 120 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=120000).pack()),
        types.InlineKeyboardButton(text="до 150 000 км",
                                   callback_data=MileageChoose(action='mileage_bounds',
                                                               answer='до 150 000 км',
                                                               mileage_left_bound=0,
                                                               mileage_right_bound=150000).pack()),
        types.InlineKeyboardButton(text="более 150 000 км", callback_data=MileageChoose(action='mileage_bounds',
                                                                                        answer='более 150 000 км',
                                                                                        mileage_left_bound=150000,
                                                                                        mileage_right_bound=0).pack()),
    )
    kb.row(
        types.InlineKeyboardButton(text="Пропустить", callback_data=MileageChoose(action='mileage_bounds',
                                                                                  answer='Пропустить',
                                                                                  mileage_left_bound=0,
                                                                                  mileage_right_bound=0).pack())
    )
    return kb.as_markup()
