from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BrandChoose(CallbackData, prefix='b'):
    action: str
    brand_auto_ru: str
    brand_encar_com: str
    answer: str


def brand_choose():
    kb = InlineKeyboardBuilder()
    kb.row(
        types.InlineKeyboardButton(text="Audi",
                                   callback_data=BrandChoose(action='brand_car', answer='Audi', brand_auto_ru='AUDI',
                                                             brand_encar_com='아우디').pack()),
        types.InlineKeyboardButton(text="BMW",
                                   callback_data=BrandChoose(action='brand_car', answer='BMW', brand_auto_ru='BMW',
                                                             brand_encar_com='BMW').pack()),
        types.InlineKeyboardButton(text="Chevrolet",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Chevrolet',
                                                             brand_auto_ru='CHEVROLET', brand_encar_com='쉐보레').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Ferrari",
                                   callback_data=BrandChoose(action='brand_car', answer='Ferrari',
                                                             brand_auto_ru='FERRARI', brand_encar_com='페라리').pack()),
        types.InlineKeyboardButton(text="Ford",
                                   callback_data=BrandChoose(action='brand_car', answer='Ford',
                                                             brand_auto_ru='FORD', brand_encar_com='포드').pack()),
        types.InlineKeyboardButton(text="Honda",
                                   callback_data=BrandChoose(action='brand_car', answer='Honda',
                                                             brand_auto_ru='HONDA', brand_encar_com='혼다').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Hyundai",
                                   callback_data=BrandChoose(action='brand_car', answer='Hyundai',
                                                             brand_auto_ru='HYUNDAI', brand_encar_com='현대').pack()),
        types.InlineKeyboardButton(text="Jaguar",
                                   callback_data=BrandChoose(action='brand_car', answer='Jaguar',
                                                             brand_auto_ru='JAGUAR', brand_encar_com='재규어').pack()),
        types.InlineKeyboardButton(text="Kia",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Kia',
                                                             brand_auto_ru='KIA', brand_encar_com='기아').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Lamborghini",
                                   callback_data=BrandChoose(action='brand_car', answer='Lamborghini',
                                                             brand_auto_ru='LAMBORGHINI', brand_encar_com='람보르기니').pack()),
        types.InlineKeyboardButton(text="Land Rover",
                                   callback_data=BrandChoose(action='brand_car', answer='Land Rover',
                                                             brand_auto_ru='LAND_ROVER', brand_encar_com='랜드로버').pack()),
        types.InlineKeyboardButton(text="Lexus",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Lexus',
                                                             brand_auto_ru='LEXUS', brand_encar_com='렉서스').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Mazda",
                                   callback_data=BrandChoose(action='brand_car', answer='Mazda',
                                                             brand_auto_ru='MAZDA', brand_encar_com='마쯔다').pack()),
        types.InlineKeyboardButton(text="Mercedes-Benz",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Mercedes-Benz',
                                                             brand_auto_ru='MERCEDES', brand_encar_com='벤츠').pack()),
        types.InlineKeyboardButton(text="Mitsubishi",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Mitsubishi',
                                                             brand_auto_ru='MITSUBISHI', brand_encar_com='미쯔비시').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Maserati",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Maserati',
                                                             brand_auto_ru='MASERATI', brand_encar_com='마세라티').pack()),
        types.InlineKeyboardButton(text="Nissan",
                                   callback_data=BrandChoose(action='brand_car', answer='Nissan',
                                                             brand_auto_ru='NISSAN', brand_encar_com='닛산').pack()),
        types.InlineKeyboardButton(text="Porsche",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Porsche',
                                                             brand_auto_ru='PORSCHE', brand_encar_com='포르쉐').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Rolls-Royce",
                                   callback_data=BrandChoose(action='brand_car', answer='Rolls-Royce',
                                                             brand_auto_ru='ROLLS_ROYCE', brand_encar_com='롤스로이스').pack()),
        types.InlineKeyboardButton(text="Subaru",
                                   callback_data=BrandChoose(action='brand_car', answer='Subaru',
                                                             brand_auto_ru='SUBARU', brand_encar_com='스바루').pack()),
        types.InlineKeyboardButton(text="Tesla",
                                   callback_data=BrandChoose(action='brand_auto_ru', answer='Tesla',
                                                             brand_auto_ru='TESLA', brand_encar_com='테슬라').pack())
    )
    kb.row(
        types.InlineKeyboardButton(text="Toyota",
                                   callback_data=BrandChoose(action='brand_car', answer='Toyota',
                                                             brand_auto_ru='TOYOTA', brand_encar_com='도요타').pack()),
        types.InlineKeyboardButton(text="Volkswagen",
                                   callback_data=BrandChoose(action='brand_car', answer='Volkswagen',
                                                             brand_auto_ru='VOLKSWAGEN', brand_encar_com='폭스바겐').pack()),
        types.InlineKeyboardButton(text="Volvo",
                                   callback_data=BrandChoose(action='brand_car', answer='Volvo',
                                                             brand_auto_ru='VOLVO',
                                                             brand_encar_com='볼보').pack())
    )
    return kb.as_markup()

