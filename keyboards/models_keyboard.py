# models_keyboard.py
from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ModelChoose(CallbackData, prefix='m'):
    action: str
    model_auto_ru: str
    model_encar_com: str
    answer: str


def model_choose(brand_auto_ru):
    """
    Generates an inline keyboard for choosing car models based on the brand.

    :param brand_auto_ru: Brand code for the car model.
    :return: InlineKeyboardMarkup: Inline keyboard with car model options.
    """
    kb = InlineKeyboardBuilder()
    if brand_auto_ru == "AUDI":
        kb.row(
            types.InlineKeyboardButton(text="A1",
                                       callback_data=ModelChoose(action='model_car', answer='A1',
                                                                 model_auto_ru='A1',
                                                                 model_encar_com='A1').pack()),
            types.InlineKeyboardButton(text="A3",
                                       callback_data=ModelChoose(action='model_car', answer='A3',
                                                                 model_auto_ru='A3',
                                                                 model_encar_com='A3').pack()),
            types.InlineKeyboardButton(text="A4",
                                       callback_data=ModelChoose(action='model_car', answer='A4', model_auto_ru='A4',
                                                                 model_encar_com='A4').pack()),
            types.InlineKeyboardButton(text="A5",
                                       callback_data=ModelChoose(action='model_car', answer='A5', model_auto_ru='A5',
                                                                 model_encar_com='A5').pack()),
            types.InlineKeyboardButton(text="A6",
                                       callback_data=ModelChoose(action='model_car', answer='A6', model_auto_ru='A6',
                                                                 model_encar_com='A6').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="A7",
                                       callback_data=ModelChoose(action='model_car', answer='A7', model_auto_ru='A7',
                                                                 model_encar_com='A7').pack()),
            types.InlineKeyboardButton(text="A8",
                                       callback_data=ModelChoose(action='model_car', answer='A8', model_auto_ru='A8',
                                                                 model_encar_com='A8').pack()),
            types.InlineKeyboardButton(text="Q2",
                                       callback_data=ModelChoose(action='model_car', answer='Q2',
                                                                 model_auto_ru='Q2',
                                                                 model_encar_com='Q2').pack()),
            types.InlineKeyboardButton(text="Q3",
                                       callback_data=ModelChoose(action='model_car', answer='Q3',
                                                                 model_auto_ru='Q3',
                                                                 model_encar_com='Q3').pack()),
            types.InlineKeyboardButton(text="Q4",
                                       callback_data=ModelChoose(action='model_car', answer='Q4', model_auto_ru='Q4',
                                                                 model_encar_com='Q4').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Q5",
                                       callback_data=ModelChoose(action='model_car', answer='Q5', model_auto_ru='Q5',
                                                                 model_encar_com='Q5').pack()),
            types.InlineKeyboardButton(text="Q6",
                                       callback_data=ModelChoose(action='model_car', answer='Q6', model_auto_ru='Q6',
                                                                 model_encar_com='Q6').pack()),
            types.InlineKeyboardButton(text="Q7",
                                       callback_data=ModelChoose(action='model_car', answer='Q7', model_auto_ru='Q7',
                                                                 model_encar_com='Q7').pack()),
            types.InlineKeyboardButton(text="Q8",
                                       callback_data=ModelChoose(action='model_car', answer='Q8', model_auto_ru='Q8',
                                                                 model_encar_com='Q8').pack()),
            types.InlineKeyboardButton(text="TT",
                                       callback_data=ModelChoose(action='model_car', answer='TT', model_auto_ru='TT',
                                                                 model_encar_com='TT').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="TTS",
                                       callback_data=ModelChoose(action='model_car', answer='TTS', model_auto_ru='TTS',
                                                                 model_encar_com='TTS').pack()),
            types.InlineKeyboardButton(text="R8",
                                       callback_data=ModelChoose(action='model_car', answer='R8',
                                                                 model_auto_ru='R8',
                                                                 model_encar_com='R8').pack()),

            types.InlineKeyboardButton(text="RS3",
                                       callback_data=ModelChoose(action='model_car', answer='RS3',
                                                                 model_auto_ru='RS3',
                                                                 model_encar_com='RS3').pack()),
            types.InlineKeyboardButton(text="RS5",
                                       callback_data=ModelChoose(action='model_car', answer='RS5', model_auto_ru='RS5',
                                                                 model_encar_com='RS5').pack()),
            types.InlineKeyboardButton(text="RS6",
                                       callback_data=ModelChoose(action='model_car', answer='RS6', model_auto_ru='RS6',
                                                                 model_encar_com='RS6').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="RS7",
                                       callback_data=ModelChoose(action='model_car', answer='RS7', model_auto_ru='RS7',
                                                                 model_encar_com='RS7').pack()),
            types.InlineKeyboardButton(text="RSQ8",
                                       callback_data=ModelChoose(action='model_car', answer='RSQ8',
                                                                 model_auto_ru='RS_Q8',
                                                                 model_encar_com='RSQ8').pack()),
            types.InlineKeyboardButton(text="S3",
                                       callback_data=ModelChoose(action='model_car', answer='S3',
                                                                 model_auto_ru='S3',
                                                                 model_encar_com='S3').pack()),
            types.InlineKeyboardButton(text="S4",
                                       callback_data=ModelChoose(action='model_car', answer='S4',
                                                                 model_auto_ru='S4',
                                                                 model_encar_com='S4').pack()),
            types.InlineKeyboardButton(text="S5",
                                       callback_data=ModelChoose(action='model_car', answer='S5', model_auto_ru='S5',
                                                                 model_encar_com='S5').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="S6",
                                       callback_data=ModelChoose(action='model_car', answer='S6', model_auto_ru='S6',
                                                                 model_encar_com='S6').pack()),
            types.InlineKeyboardButton(text="S7",
                                       callback_data=ModelChoose(action='model_car', answer='S7', model_auto_ru='S7',
                                                                 model_encar_com='S7').pack()),
            types.InlineKeyboardButton(text="S8",
                                       callback_data=ModelChoose(action='model_car', answer='S8', model_auto_ru='S8',
                                                                 model_encar_com='S8').pack()),
            types.InlineKeyboardButton(text="SQ5",
                                       callback_data=ModelChoose(action='model_car', answer='SQ5', model_auto_ru='SQ5',
                                                                 model_encar_com='SQ5').pack()),
            types.InlineKeyboardButton(text="SQ8",
                                       callback_data=ModelChoose(action='model_car', answer='SQ8',
                                                                 model_auto_ru='SQ8',
                                                                 model_encar_com='SQ8').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="RS e-tron GT",
                                       callback_data=ModelChoose(action='model_car', answer='RS e-tron GT',
                                                                 model_auto_ru='RS_E_TRON_GT',
                                                                 model_encar_com='RS e-트론 GT').pack()),
            types.InlineKeyboardButton(text="e-tron",
                                       callback_data=ModelChoose(action='model_car', answer='e-tron',
                                                                 model_auto_ru='E_TRON',
                                                                 model_encar_com='e-트론').pack()),
            types.InlineKeyboardButton(text="e-tron GT",
                                       callback_data=ModelChoose(action='model_car', answer='e-tron GT',
                                                                 model_auto_ru='E_TRON_GT',
                                                                 model_encar_com='e-트론 GT').pack())
        )
    elif brand_auto_ru == "BENTLEY":
        kb.row(
            types.InlineKeyboardButton(text="Bentayga",
                                       callback_data=ModelChoose(action='model_car', answer='Bentayga',
                                                                 model_auto_ru='BENTAYGA',
                                                                 model_encar_com='벤테이가').pack()),
            types.InlineKeyboardButton(text="Continental",
                                       callback_data=ModelChoose(action='model_car', answer='Continental',
                                                                 model_auto_ru='CONTINENTAL',
                                                                 model_encar_com='컨티넨탈').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Flying Spur",
                                       callback_data=ModelChoose(action='model_car', answer='Flying Spur',
                                                                 model_auto_ru='CONTINENTAL_FLYING_SPUR',
                                                                 model_encar_com='플라잉스퍼').pack()),
            types.InlineKeyboardButton(text="Mulsanne",
                                       callback_data=ModelChoose(action='model_car', answer='Mulsanne',
                                                                 model_auto_ru='MULSANNE',
                                                                 model_encar_com='뮬산').pack())
        )
    elif brand_auto_ru == "BMW":
        kb.row(
            types.InlineKeyboardButton(text="1 серии",
                                       callback_data=ModelChoose(action='model_car', answer='1 серии',
                                                                 model_auto_ru='1ER',
                                                                 model_encar_com='1시리즈').pack()),
            types.InlineKeyboardButton(text="2 серии",
                                       callback_data=ModelChoose(action='model_car', answer='2 серии',
                                                                 model_auto_ru='2ER',
                                                                 model_encar_com='2시리즈').pack()),
            types.InlineKeyboardButton(text="3 серии",
                                       callback_data=ModelChoose(action='model_car', answer='3 серии',
                                                                 model_auto_ru='3ER',
                                                                 model_encar_com='3시리즈').pack()),
            types.InlineKeyboardButton(text="4 серии",
                                       callback_data=ModelChoose(action='model_car', answer='4 серии',
                                                                 model_auto_ru='4',
                                                                 model_encar_com='4시리즈').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="5 серии",
                                       callback_data=ModelChoose(action='model_car', answer='5 серии',
                                                                 model_auto_ru='5ER',
                                                                 model_encar_com='5시리즈').pack()),
            types.InlineKeyboardButton(text="6 серии",
                                       callback_data=ModelChoose(action='model_car', answer='6 серии',
                                                                 model_auto_ru='6ER',
                                                                 model_encar_com='6시리즈').pack()),
            types.InlineKeyboardButton(text="7 серии",
                                       callback_data=ModelChoose(action='model_car', answer='7 серии',
                                                                 model_auto_ru='7ER',
                                                                 model_encar_com='7시리즈').pack()),
            types.InlineKeyboardButton(text="8 серии",
                                       callback_data=ModelChoose(action='model_car', answer='8 серии',
                                                                 model_auto_ru='8ER',
                                                                 model_encar_com='8시리즈').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="1M",
                                       callback_data=ModelChoose(action='model_car', answer='1M',
                                                                 model_auto_ru='1M',
                                                                 model_encar_com='1M').pack()),
            types.InlineKeyboardButton(text="M2",
                                       callback_data=ModelChoose(action='model_car', answer='M2',
                                                                 model_auto_ru='M2',
                                                                 model_encar_com='M2').pack()),
            types.InlineKeyboardButton(text="M3",
                                       callback_data=ModelChoose(action='model_car', answer='M3',
                                                                 model_auto_ru='M3',
                                                                 model_encar_com='M3').pack()),
            types.InlineKeyboardButton(text="M4",
                                       callback_data=ModelChoose(action='model_car', answer='M4',
                                                                 model_auto_ru='M4',
                                                                 model_encar_com='M4').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="M5",
                                       callback_data=ModelChoose(action='model_car', answer='M5',
                                                                 model_auto_ru='M5',
                                                                 model_encar_com='M5').pack()),
            types.InlineKeyboardButton(text="M6",
                                       callback_data=ModelChoose(action='model_car', answer='M6',
                                                                 model_auto_ru='M6',
                                                                 model_encar_com='M6').pack()),
            types.InlineKeyboardButton(text="M8",
                                       callback_data=ModelChoose(action='model_car', answer='M8',
                                                                 model_auto_ru='M8',
                                                                 model_encar_com='M8').pack()),
            types.InlineKeyboardButton(text="X1",
                                       callback_data=ModelChoose(action='model_car', answer='X1',
                                                                 model_auto_ru='X1',
                                                                 model_encar_com='X1').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="X2",
                                       callback_data=ModelChoose(action='model_car', answer='X2',
                                                                 model_auto_ru='X2',
                                                                 model_encar_com='X2').pack()),
            types.InlineKeyboardButton(text="X3",
                                       callback_data=ModelChoose(action='model_car', answer='X3',
                                                                 model_auto_ru='X3',
                                                                 model_encar_com='X3').pack()),
            types.InlineKeyboardButton(text="X4",
                                       callback_data=ModelChoose(action='model_car', answer='X4',
                                                                 model_auto_ru='X4',
                                                                 model_encar_com='X4').pack()),
            types.InlineKeyboardButton(text="X5",
                                       callback_data=ModelChoose(action='model_car', answer='X5',
                                                                 model_auto_ru='X5',
                                                                 model_encar_com='X5').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="X6",
                                       callback_data=ModelChoose(action='model_car', answer='X6',
                                                                 model_auto_ru='X6',
                                                                 model_encar_com='X6').pack()),
            types.InlineKeyboardButton(text="X7",
                                       callback_data=ModelChoose(action='model_car', answer='X7',
                                                                 model_auto_ru='X7',
                                                                 model_encar_com='X7').pack()),
            types.InlineKeyboardButton(text="X3 M",
                                       callback_data=ModelChoose(action='model_car', answer='X3 M',
                                                                 model_auto_ru='X3_M',
                                                                 model_encar_com='X3M').pack()),
            types.InlineKeyboardButton(text="X4 M",
                                       callback_data=ModelChoose(action='model_car', answer='X4 M',
                                                                 model_auto_ru='X4_M',
                                                                 model_encar_com='X4M').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="X5 M",
                                       callback_data=ModelChoose(action='model_car', answer='X5 M',
                                                                 model_auto_ru='X5_M',
                                                                 model_encar_com='X5M').pack()),
            types.InlineKeyboardButton(text="X6 M",
                                       callback_data=ModelChoose(action='model_car', answer='X6 M',
                                                                 model_auto_ru='X6_M',
                                                                 model_encar_com='X6M').pack()),
            types.InlineKeyboardButton(text="XM",
                                       callback_data=ModelChoose(action='model_car', answer='XM',
                                                                 model_auto_ru='XM',
                                                                 model_encar_com='XM').pack()),
            types.InlineKeyboardButton(text="Z3",
                                       callback_data=ModelChoose(action='model_car', answer='Z3',
                                                                 model_auto_ru='Z3',
                                                                 model_encar_com='Z3').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Z4",
                                       callback_data=ModelChoose(action='model_car', answer='Z4',
                                                                 model_auto_ru='Z4',
                                                                 model_encar_com='Z4').pack()),
            types.InlineKeyboardButton(text="i3",
                                       callback_data=ModelChoose(action='model_car', answer='i3',
                                                                 model_auto_ru='I3',
                                                                 model_encar_com='i3').pack()),
            types.InlineKeyboardButton(text="i4",
                                       callback_data=ModelChoose(action='model_car', answer='i4',
                                                                 model_auto_ru='I4',
                                                                 model_encar_com='i4').pack()),
            types.InlineKeyboardButton(text="i5",
                                       callback_data=ModelChoose(action='model_car', answer='i5',
                                                                 model_auto_ru='I5',
                                                                 model_encar_com='i5').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="i7",
                                       callback_data=ModelChoose(action='model_car', answer='i7',
                                                                 model_auto_ru='I7',
                                                                 model_encar_com='i7').pack()),
            types.InlineKeyboardButton(text="i8",
                                       callback_data=ModelChoose(action='model_car', answer='i8',
                                                                 model_auto_ru='I8',
                                                                 model_encar_com='i8').pack()),
            types.InlineKeyboardButton(text="iX3",
                                       callback_data=ModelChoose(action='model_car', answer='iX3',
                                                                 model_auto_ru='IX3',
                                                                 model_encar_com='iX3').pack()),
            types.InlineKeyboardButton(text="iX",
                                       callback_data=ModelChoose(action='model_car', answer='iX',
                                                                 model_auto_ru='IX',
                                                                 model_encar_com='iX').pack())
        )
    elif brand_auto_ru == "CHEVROLET":
        kb.row(
            types.InlineKeyboardButton(text="Aveo",
                                       callback_data=ModelChoose(action='model_car', answer='Aveo',
                                                                 model_auto_ru='AVEO',
                                                                 model_encar_com='아베오').pack()),
            types.InlineKeyboardButton(text="Bolt",
                                       callback_data=ModelChoose(action='model_car', answer='Bolt',
                                                                 model_auto_ru='BOLT',
                                                                 model_encar_com='볼트 EV').pack()),
            types.InlineKeyboardButton(text="Captiva",
                                       callback_data=ModelChoose(action='model_car', answer='Captiva',
                                                                 model_auto_ru='CAPTIVA',
                                                                 model_encar_com='캡티바').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Colorado",
                                       callback_data=ModelChoose(action='model_car', answer='Colorado',
                                                                 model_auto_ru='COLORADO',
                                                                 model_encar_com='콜로라도').pack()),
            types.InlineKeyboardButton(text="Cruze",
                                       callback_data=ModelChoose(action='model_car', answer='Cruze',
                                                                 model_auto_ru='CRUZE',
                                                                 model_encar_com='크루즈').pack()),
            types.InlineKeyboardButton(text="Camaro",
                                       callback_data=ModelChoose(action='model_car', answer='Camaro',
                                                                 model_auto_ru='CAMARO',
                                                                 model_encar_com='카마로').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Equinox",
                                       callback_data=ModelChoose(action='model_car', answer='Equinox',
                                                                 model_auto_ru='EQUINOX',
                                                                 model_encar_com='이쿼녹스').pack()),
            types.InlineKeyboardButton(text="Impala",
                                       callback_data=ModelChoose(action='model_car', answer='Impala',
                                                                 model_auto_ru='IMPALA',
                                                                 model_encar_com='임팔라').pack()),
            types.InlineKeyboardButton(text="Lacetti",
                                       callback_data=ModelChoose(action='model_car', answer='Lacetti',
                                                                 model_auto_ru='LACETTI',
                                                                 model_encar_com='라세티').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Malibu",
                                       callback_data=ModelChoose(action='model_car', answer='Malibu',
                                                                 model_auto_ru='MALIBU',
                                                                 model_encar_com='말리부').pack()),
            types.InlineKeyboardButton(text="Matiz",
                                       callback_data=ModelChoose(action='model_car', answer='Matiz',
                                                                 model_auto_ru='MATIZ',
                                                                 model_encar_com='마티즈').pack()),
            types.InlineKeyboardButton(text="Orlando",
                                       callback_data=ModelChoose(action='model_car', answer='Orlando',
                                                                 model_auto_ru='ORLANDO',
                                                                 model_encar_com='올란도').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Spark",
                                       callback_data=ModelChoose(action='model_car', answer='Spark',
                                                                 model_auto_ru='SPARK',
                                                                 model_encar_com='스파크').pack()),
            types.InlineKeyboardButton(text="Tahoe",
                                       callback_data=ModelChoose(action='model_car', answer='Tahoe',
                                                                 model_auto_ru='TAHOE',
                                                                 model_encar_com='타호').pack()),
            types.InlineKeyboardButton(text="Tracker",
                                       callback_data=ModelChoose(action='model_car', answer='Tracker',
                                                                 model_auto_ru='TRACKER',
                                                                 model_encar_com='트랙스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="TrailBlazer",
                                       callback_data=ModelChoose(action='model_car', answer='TrailBlazer',
                                                                 model_auto_ru='TRAILBLAZER',
                                                                 model_encar_com='트레일블레이저').pack()),
            types.InlineKeyboardButton(text="Traverse",
                                       callback_data=ModelChoose(action='model_car', answer='Traverse',
                                                                 model_auto_ru='TRAVERSE',
                                                                 model_encar_com='트래버스').pack()),
            types.InlineKeyboardButton(text="Volt",
                                       callback_data=ModelChoose(action='model_car', answer='Volt',
                                                                 model_auto_ru='VOLT',
                                                                 model_encar_com='볼트(Volt_)').pack())
        )
    elif brand_auto_ru == "FERRARI":
        kb.row(
            types.InlineKeyboardButton(text="296",
                                       callback_data=ModelChoose(action='model_car', answer='296',
                                                                 model_auto_ru='296_GTB',
                                                                 model_encar_com='296').pack()),
            types.InlineKeyboardButton(text="360",
                                       callback_data=ModelChoose(action='model_car', answer='360',
                                                                 model_auto_ru='360_MODENA',
                                                                 model_encar_com='360').pack()),
            types.InlineKeyboardButton(text="456",
                                       callback_data=ModelChoose(action='model_car', answer='456',
                                                                 model_auto_ru='456',
                                                                 model_encar_com='456').pack()),
            types.InlineKeyboardButton(text="458",
                                       callback_data=ModelChoose(action='model_car', answer='458',
                                                                 model_auto_ru='458_ITALIA',
                                                                 model_encar_com='458').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="488",
                                       callback_data=ModelChoose(action='model_car', answer='488',
                                                                 model_auto_ru='488',
                                                                 model_encar_com='488').pack()),
            types.InlineKeyboardButton(text="599",
                                       callback_data=ModelChoose(action='model_car', answer='599',
                                                                 model_auto_ru='599',
                                                                 model_encar_com='599').pack()),
            types.InlineKeyboardButton(text="812",
                                       callback_data=ModelChoose(action='model_car', answer='812',
                                                                 model_auto_ru='812_SUPERFAST',
                                                                 model_encar_com='812').pack()),
            types.InlineKeyboardButton(text="F8",
                                       callback_data=ModelChoose(action='model_car', answer='F8',
                                                                 model_auto_ru='F8_TRIBUTO',
                                                                 model_encar_com='F8').pack())

        )
        kb.row(
            types.InlineKeyboardButton(text="F430",
                                       callback_data=ModelChoose(action='model_car', answer='F430',
                                                                 model_auto_ru='F430',
                                                                 model_encar_com='F430').pack()),

            types.InlineKeyboardButton(text="FF",
                                       callback_data=ModelChoose(action='model_car', answer='FF',
                                                                 model_auto_ru='FF',
                                                                 model_encar_com='FF').pack()),
            types.InlineKeyboardButton(text="SF90",
                                       callback_data=ModelChoose(action='model_car', answer='SF90',
                                                                 model_auto_ru='SF90_STRADALE',
                                                                 model_encar_com='SF90').pack()),
            types.InlineKeyboardButton(text="Roma",
                                       callback_data=ModelChoose(action='model_car', answer='Roma',
                                                                 model_auto_ru='ROMA',
                                                                 model_encar_com='로마').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="California",
                                       callback_data=ModelChoose(action='model_car', answer='California',
                                                                 model_auto_ru='CALIFORNIA',
                                                                 model_encar_com='캘리포니아').pack()),
            types.InlineKeyboardButton(text="F12berlinetta",
                                       callback_data=ModelChoose(action='model_car', answer='F12berlinetta',
                                                                 model_auto_ru='F12BERLINETTA',
                                                                 model_encar_com='F12 베를리네타').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GTC4Lusso",
                                       callback_data=ModelChoose(action='model_car', answer='GTC4Lusso',
                                                                 model_auto_ru='GTC4LUSSO',
                                                                 model_encar_com='GTC4 루쏘').pack()),
            types.InlineKeyboardButton(text="Portofino",
                                       callback_data=ModelChoose(action='model_car', answer='Portofino',
                                                                 model_auto_ru='PORTOFINO',
                                                                 model_encar_com='포르토피노').pack())
        )
    elif brand_auto_ru == "FORD":
        kb.row(
            types.InlineKeyboardButton(text="Bronco",
                                       callback_data=ModelChoose(action='model_car', answer='Bronco',
                                                                 model_auto_ru='BRONCO',
                                                                 model_encar_com='브롱코').pack()),
            types.InlineKeyboardButton(text="Explorer",
                                       callback_data=ModelChoose(action='model_car', answer='Explorer',
                                                                 model_auto_ru='EXPLORER',
                                                                 model_encar_com='익스플로러').pack()),
            types.InlineKeyboardButton(text="Expedition",
                                       callback_data=ModelChoose(action='model_car', answer='Expedition',
                                                                 model_auto_ru='EXPEDITION',
                                                                 model_encar_com='익스페디션').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="F-150",
                                       callback_data=ModelChoose(action='model_car', answer='F-150',
                                                                 model_auto_ru='F_150',
                                                                 model_encar_com='F150').pack()),
            types.InlineKeyboardButton(text="F-350",
                                       callback_data=ModelChoose(action='model_car', answer='F-350',
                                                                 model_auto_ru='F_350',
                                                                 model_encar_com='F350').pack()),
            types.InlineKeyboardButton(text="Focus",
                                       callback_data=ModelChoose(action='model_car', answer='Focus',
                                                                 model_auto_ru='FOCUS',
                                                                 model_encar_com='포커스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Fusion",
                                       callback_data=ModelChoose(action='model_car', answer='Fusion',
                                                                 model_auto_ru='FUSION_NA',
                                                                 model_encar_com='퓨전').pack()),
            types.InlineKeyboardButton(text="Kuga",
                                       callback_data=ModelChoose(action='model_car', answer='Kuga',
                                                                 model_auto_ru='KUGA',
                                                                 model_encar_com='쿠가').pack()),
            types.InlineKeyboardButton(text="Mondeo",
                                       callback_data=ModelChoose(action='model_car', answer='Mondeo',
                                                                 model_auto_ru='MONDEO',
                                                                 model_encar_com='몬데오').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Mustang",
                                       callback_data=ModelChoose(action='model_car', answer='Mustang',
                                                                 model_auto_ru='MUSTANG',
                                                                 model_encar_com='머스탱').pack()),
            types.InlineKeyboardButton(text="Ranger",
                                       callback_data=ModelChoose(action='model_car', answer='Ranger',
                                                                 model_auto_ru='RANGER',
                                                                 model_encar_com='레인저').pack()),
            types.InlineKeyboardButton(text="Taurus",
                                       callback_data=ModelChoose(action='model_car', answer='Taurus',
                                                                 model_auto_ru='TAURUS',
                                                                 model_encar_com='토러스').pack())
        )
    elif brand_auto_ru == "GENESIS":
        kb.row(
            types.InlineKeyboardButton(text="G70",
                                       callback_data=ModelChoose(action='model_car', answer='G70',
                                                                 model_auto_ru='G70',
                                                                 model_encar_com='G70').pack()),
            types.InlineKeyboardButton(text="G80",
                                       callback_data=ModelChoose(action='model_car', answer='G80',
                                                                 model_auto_ru='G80',
                                                                 model_encar_com='G80').pack()),
            types.InlineKeyboardButton(text="G90",
                                       callback_data=ModelChoose(action='model_car', answer='G90',
                                                                 model_auto_ru='G90',
                                                                 model_encar_com='G90').pack()),
            types.InlineKeyboardButton(text="GV60",
                                       callback_data=ModelChoose(action='model_car', answer='GV60',
                                                                 model_auto_ru='GV60',
                                                                 model_encar_com='GV60').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GV70",
                                       callback_data=ModelChoose(action='model_car', answer='GV70',
                                                                 model_auto_ru='GV70',
                                                                 model_encar_com='GV70').pack()),
            types.InlineKeyboardButton(text="GV80",
                                       callback_data=ModelChoose(action='model_car', answer='GV80',
                                                                 model_auto_ru='GV80',
                                                                 model_encar_com='GV80').pack()),
            types.InlineKeyboardButton(text="EQ900",
                                       callback_data=ModelChoose(action='model_car', answer='EQ900',
                                                                 model_auto_ru='EQ900',
                                                                 model_encar_com='EQ900').pack())
        )
    elif brand_auto_ru == "HONDA":
        kb.row(
            types.InlineKeyboardButton(text="Accord",
                                       callback_data=ModelChoose(action='model_car', answer='Accord',
                                                                 model_auto_ru='ACCORD',
                                                                 model_encar_com='어코드').pack()),
            types.InlineKeyboardButton(text="CR-V",
                                       callback_data=ModelChoose(action='model_car', answer='CR-V',
                                                                 model_auto_ru='CR_V',
                                                                 model_encar_com='CR-V').pack()),
            types.InlineKeyboardButton(text="CR-Z",
                                       callback_data=ModelChoose(action='model_car', answer='CR-Z',
                                                                 model_auto_ru='CR_Z',
                                                                 model_encar_com='CR-Z').pack()),
            types.InlineKeyboardButton(text="S2000",
                                       callback_data=ModelChoose(action='model_car', answer='S2000',
                                                                 model_auto_ru='S2000',
                                                                 model_encar_com='S2000').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Civic",
                                       callback_data=ModelChoose(action='model_car', answer='Civic',
                                                                 model_auto_ru='CIVIC',
                                                                 model_encar_com='시빅').pack()),
            types.InlineKeyboardButton(text="Odyssey",
                                       callback_data=ModelChoose(action='model_car', answer='Odyssey',
                                                                 model_auto_ru='ODYSSEY_NA',
                                                                 model_encar_com='오딧세이').pack()),
            types.InlineKeyboardButton(text="Pilot",
                                       callback_data=ModelChoose(action='model_car', answer='Pilot',
                                                                 model_auto_ru='PILOT',
                                                                 model_encar_com='파일럿').pack()),
            types.InlineKeyboardButton(text="S660",
                                       callback_data=ModelChoose(action='model_car', answer='S660',
                                                                 model_auto_ru='S660',
                                                                 model_encar_com='S660').pack())
        )
    elif brand_auto_ru == "HYUNDAI":
        kb.row(
            types.InlineKeyboardButton(text="Aslan",
                                       callback_data=ModelChoose(action='model_car', answer='Aslan',
                                                                 model_auto_ru='ASLAN',
                                                                 model_encar_com='아슬란').pack()),
            types.InlineKeyboardButton(text="Avante",
                                       callback_data=ModelChoose(action='model_car', answer='Avante',
                                                                 model_auto_ru='AVANTE',
                                                                 model_encar_com='아반떼').pack()),
            types.InlineKeyboardButton(text="Casper",
                                       callback_data=ModelChoose(action='model_car', answer='Casper',
                                                                 model_auto_ru='CASPER',
                                                                 model_encar_com='캐스퍼').pack()),
            types.InlineKeyboardButton(text="Equus",
                                       callback_data=ModelChoose(action='model_car', answer='Equus',
                                                                 model_auto_ru='EQUUS',
                                                                 model_encar_com='에쿠스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Galloper",
                                       callback_data=ModelChoose(action='model_car', answer='Galloper',
                                                                 model_auto_ru='GALLOPER',
                                                                 model_encar_com='갤로퍼').pack()),
            types.InlineKeyboardButton(text="Genesis",
                                       callback_data=ModelChoose(action='model_car', answer='Genesis',
                                                                 model_auto_ru='GENESIS',
                                                                 model_encar_com='제네시스').pack()),
            types.InlineKeyboardButton(text="Grandeur",
                                       callback_data=ModelChoose(action='model_car', answer='Grandeur',
                                                                 model_auto_ru='GRANDEUR',
                                                                 model_encar_com='그랜저').pack()),
            types.InlineKeyboardButton(text="i30",
                                       callback_data=ModelChoose(action='model_car', answer='i30',
                                                                 model_auto_ru='I30',
                                                                 model_encar_com='i30').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="i40",
                                       callback_data=ModelChoose(action='model_car', answer='i40',
                                                                 model_auto_ru='I40',
                                                                 model_encar_com='i40').pack()),
            types.InlineKeyboardButton(text="IONIQ",
                                       callback_data=ModelChoose(action='model_car', answer='IONIQ',
                                                                 model_auto_ru='IONIQ',
                                                                 model_encar_com='아이오닉').pack()),
            types.InlineKeyboardButton(text="IONIQ 5",
                                       callback_data=ModelChoose(action='model_car', answer='IONIQ 5',
                                                                 model_auto_ru='IONIQ_5',
                                                                 model_encar_com='아이오닉5').pack()),
            types.InlineKeyboardButton(text="Kona",
                                       callback_data=ModelChoose(action='model_car', answer='Kona',
                                                                 model_auto_ru='KONA',
                                                                 model_encar_com='코나').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Maxcruz",
                                       callback_data=ModelChoose(action='model_car', answer='Maxcruz',
                                                                 model_auto_ru='MAXCRUZ',
                                                                 model_encar_com='맥스크루즈').pack()),
            types.InlineKeyboardButton(text="Nexo",
                                       callback_data=ModelChoose(action='model_car', answer='Nexo',
                                                                 model_auto_ru='NEXO',
                                                                 model_encar_com='넥쏘').pack()),
            types.InlineKeyboardButton(text="Palisade",
                                       callback_data=ModelChoose(action='model_car', answer='Palisade',
                                                                 model_auto_ru='PALISADE',
                                                                 model_encar_com='팰리세이드').pack()),
            types.InlineKeyboardButton(text="Santa Fe",
                                       callback_data=ModelChoose(action='model_car', answer='Santa Fe',
                                                                 model_auto_ru='SANTA_FE',
                                                                 model_encar_com='싼타페').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Sonata",
                                       callback_data=ModelChoose(action='model_car', answer='Sonata',
                                                                 model_auto_ru='SONATA',
                                                                 model_encar_com='쏘나타').pack()),
            types.InlineKeyboardButton(text="Starex",
                                       callback_data=ModelChoose(action='model_car', answer='Starex',
                                                                 model_auto_ru='STAREX',
                                                                 model_encar_com='스타렉스').pack()),
            types.InlineKeyboardButton(text="Staria",
                                       callback_data=ModelChoose(action='model_car', answer='Staria',
                                                                 model_auto_ru='STARIA',
                                                                 model_encar_com='스타리아').pack()),
            types.InlineKeyboardButton(text="Tucson",
                                       callback_data=ModelChoose(action='model_car', answer='Tucson',
                                                                 model_auto_ru='TUCSON',
                                                                 model_encar_com='투싼').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Verna",
                                       callback_data=ModelChoose(action='model_car', answer='Verna',
                                                                 model_auto_ru='VERNA',
                                                                 model_encar_com='베르나').pack()),
            types.InlineKeyboardButton(text="Veloster",
                                       callback_data=ModelChoose(action='model_car', answer='Veloster',
                                                                 model_auto_ru='VELOSTER',
                                                                 model_encar_com='벨로스터').pack()),
            types.InlineKeyboardButton(text="Venue",
                                       callback_data=ModelChoose(action='model_car', answer='Venue',
                                                                 model_auto_ru='VENUE',
                                                                 model_encar_com='베뉴').pack()),
            types.InlineKeyboardButton(text="Veracruz",
                                       callback_data=ModelChoose(action='model_car', answer='Veracruz',
                                                                 model_auto_ru='VERACRUZ',
                                                                 model_encar_com='베라크루즈').pack())
        )
    elif brand_auto_ru == "JAGUAR":
        kb.row(
            types.InlineKeyboardButton(text="E-Pace",
                                       callback_data=ModelChoose(action='model_car', answer='E-Pace',
                                                                 model_auto_ru='E_PACE',
                                                                 model_encar_com='E-PACE').pack()),
            types.InlineKeyboardButton(text="F-Pace",
                                       callback_data=ModelChoose(action='model_car', answer='F-Pace',
                                                                 model_auto_ru='F_PACE',
                                                                 model_encar_com='F-PACE').pack()),
            types.InlineKeyboardButton(text="F-Type",
                                       callback_data=ModelChoose(action='model_car', answer='F-Type',
                                                                 model_auto_ru='F_TYPE',
                                                                 model_encar_com='F-TYPE').pack()),
            types.InlineKeyboardButton(text="I-Pace",
                                       callback_data=ModelChoose(action='model_car', answer='I-Pace',
                                                                 model_auto_ru='I_PACE',
                                                                 model_encar_com='I-PACE').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="S-Type",
                                       callback_data=ModelChoose(action='model_car', answer='S-Type',
                                                                 model_auto_ru='S_TYPE',
                                                                 model_encar_com='S-TYPE').pack()),
            types.InlineKeyboardButton(text="X-Type",
                                       callback_data=ModelChoose(action='model_car', answer='X-Type',
                                                                 model_auto_ru='X_TYPE',
                                                                 model_encar_com='X-TYPE').pack()),
            types.InlineKeyboardButton(text="XE",
                                       callback_data=ModelChoose(action='model_car', answer='XE',
                                                                 model_auto_ru='XE',
                                                                 model_encar_com='XE').pack()),
            types.InlineKeyboardButton(text="XF",
                                       callback_data=ModelChoose(action='model_car', answer='XF',
                                                                 model_auto_ru='XF',
                                                                 model_encar_com='XF').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="XJ",
                                       callback_data=ModelChoose(action='model_car', answer='XJ',
                                                                 model_auto_ru='XJ',
                                                                 model_encar_com='XJ').pack()),
            types.InlineKeyboardButton(text="XJR",
                                       callback_data=ModelChoose(action='model_car', answer='XJR',
                                                                 model_auto_ru='XJR',
                                                                 model_encar_com='XJR').pack()),
            types.InlineKeyboardButton(text="XKR",
                                       callback_data=ModelChoose(action='model_car', answer='XKR',
                                                                 model_auto_ru='XKR',
                                                                 model_encar_com='XKR').pack())
        )
    elif brand_auto_ru == "KIA":
        kb.row(
            types.InlineKeyboardButton(text="Carnival",
                                       callback_data=ModelChoose(action='model_car', answer='Carnival',
                                                                 model_auto_ru='CARNIVAL',
                                                                 model_encar_com='카니발').pack()),
            types.InlineKeyboardButton(text="Carens",
                                       callback_data=ModelChoose(action='model_car', answer='Carens',
                                                                 model_auto_ru='CARENS',
                                                                 model_encar_com='카렌스').pack()),
            types.InlineKeyboardButton(text="EV6",
                                       callback_data=ModelChoose(action='model_car', answer='EV6',
                                                                 model_auto_ru='EV6',
                                                                 model_encar_com='EV6').pack()),
            types.InlineKeyboardButton(text="EV9",
                                       callback_data=ModelChoose(action='model_car', answer='EV9',
                                                                 model_auto_ru='EV9',
                                                                 model_encar_com='EV9').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Forte",
                                       callback_data=ModelChoose(action='model_car', answer='Forte',
                                                                 model_auto_ru='FORTE',
                                                                 model_encar_com='포르테').pack()),
            types.InlineKeyboardButton(text="K3",
                                       callback_data=ModelChoose(action='model_car', answer='K3',
                                                                 model_auto_ru='K3',
                                                                 model_encar_com='K3').pack()),
            types.InlineKeyboardButton(text="K5",
                                       callback_data=ModelChoose(action='model_car', answer='K5',
                                                                 model_auto_ru='K5',
                                                                 model_encar_com='K5').pack()),
            types.InlineKeyboardButton(text="K7",
                                       callback_data=ModelChoose(action='model_car', answer='K7',
                                                                 model_auto_ru='K7',
                                                                 model_encar_com='K7').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="K8",
                                       callback_data=ModelChoose(action='model_car', answer='K8',
                                                                 model_auto_ru='K8',
                                                                 model_encar_com='K8').pack()),
            types.InlineKeyboardButton(text="K9",
                                       callback_data=ModelChoose(action='model_car', answer='K9',
                                                                 model_auto_ru='K9',
                                                                 model_encar_com='K9').pack()),
            types.InlineKeyboardButton(text="Lotze",
                                       callback_data=ModelChoose(action='model_car', answer='Lotze',
                                                                 model_auto_ru='LOTZE',
                                                                 model_encar_com='로체').pack()),
            types.InlineKeyboardButton(text="Mohave",
                                       callback_data=ModelChoose(action='model_car', answer='Mohave',
                                                                 model_auto_ru='MOHAVES',
                                                                 model_encar_com='모하비').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Morning",
                                       callback_data=ModelChoose(action='model_car', answer='Morning',
                                                                 model_auto_ru='MORNING',
                                                                 model_encar_com='모닝').pack()),
            types.InlineKeyboardButton(text="Niro",
                                       callback_data=ModelChoose(action='model_car', answer='Niro',
                                                                 model_auto_ru='NIRO',
                                                                 model_encar_com='니로').pack()),
            types.InlineKeyboardButton(text="Opirus",
                                       callback_data=ModelChoose(action='model_car', answer='Opirus',
                                                                 model_auto_ru='OPIRUS',
                                                                 model_encar_com='오피러스').pack()),
            types.InlineKeyboardButton(text="Potentia",
                                       callback_data=ModelChoose(action='model_car', answer='Potentia',
                                                                 model_auto_ru='POTENTIA',
                                                                 model_encar_com='포텐샤').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Pride",
                                       callback_data=ModelChoose(action='model_car', answer='Pride',
                                                                 model_auto_ru='PRIDE',
                                                                 model_encar_com='프라이드').pack()),
            types.InlineKeyboardButton(text="Ray",
                                       callback_data=ModelChoose(action='model_car', answer='Ray',
                                                                 model_auto_ru='RAY',
                                                                 model_encar_com='레이').pack()),
            types.InlineKeyboardButton(text="Seltos",
                                       callback_data=ModelChoose(action='model_car', answer='Seltos',
                                                                 model_auto_ru='SELTOS',
                                                                 model_encar_com='셀토스').pack()),
            types.InlineKeyboardButton(text="Sorento",
                                       callback_data=ModelChoose(action='model_car', answer='Sorento',
                                                                 model_auto_ru='SORENTO',
                                                                 model_encar_com='쏘렌토').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Soul",
                                       callback_data=ModelChoose(action='model_car', answer='Soul',
                                                                 model_auto_ru='SOUL',
                                                                 model_encar_com='쏘울').pack()),
            types.InlineKeyboardButton(text="Sportage",
                                       callback_data=ModelChoose(action='model_car', answer='Sportage',
                                                                 model_auto_ru='SPORTAGE',
                                                                 model_encar_com='스포티지').pack()),
            types.InlineKeyboardButton(text="Stinger",
                                       callback_data=ModelChoose(action='model_car', answer='Stinger',
                                                                 model_auto_ru='STINGER',
                                                                 model_encar_com='스팅어').pack()),
            types.InlineKeyboardButton(text="Stonic",
                                       callback_data=ModelChoose(action='model_car', answer='Stonic',
                                                                 model_auto_ru='STONIC',
                                                                 model_encar_com='스토닉').pack())
        )
    elif brand_auto_ru == "LAMBORGHINI":
        kb.row(
            types.InlineKeyboardButton(text="Aventador",
                                       callback_data=ModelChoose(action='model_car', answer='Aventador',
                                                                 model_auto_ru='AVENTADOR',
                                                                 model_encar_com='아벤타도르').pack()),
            types.InlineKeyboardButton(text="Gallardo",
                                       callback_data=ModelChoose(action='model_car', answer='Gallardo',
                                                                 model_auto_ru='GALLARDO',
                                                                 model_encar_com='가야르도').pack()),
        )
        kb.row(
            types.InlineKeyboardButton(text="Huracan",
                                       callback_data=ModelChoose(action='model_car', answer='Huracan',
                                                                 model_auto_ru='HURACAN',
                                                                 model_encar_com='우라칸').pack()),
            types.InlineKeyboardButton(text="Murcielago",
                                       callback_data=ModelChoose(action='model_car', answer='Murcielago',
                                                                 model_auto_ru='MURCIELAGO',
                                                                 model_encar_com='무르시엘라고').pack()),

            types.InlineKeyboardButton(text="Urus",
                                       callback_data=ModelChoose(action='model_car', answer='Urus',
                                                                 model_auto_ru='URUS',
                                                                 model_encar_com='우루스').pack())
        )
    elif brand_auto_ru == "LAND_ROVER":
        kb.row(
            types.InlineKeyboardButton(text="Discovery",
                                       callback_data=ModelChoose(action='model_car', answer='Discovery',
                                                                 model_auto_ru='DISCOVERY',
                                                                 model_encar_com='디스커버리').pack()),
            types.InlineKeyboardButton(text="Defender",
                                       callback_data=ModelChoose(action='model_car', answer='Defender',
                                                                 model_auto_ru='DEFENDER',
                                                                 model_encar_com='디펜더').pack()),
            types.InlineKeyboardButton(text="Evoque",
                                       callback_data=ModelChoose(action='model_car', answer='Evoque',
                                                                 model_auto_ru='EVOQUE',
                                                                 model_encar_com='레인지로버 이보크').pack()),

        )
        kb.row(
            types.InlineKeyboardButton(text="Freelander",
                                       callback_data=ModelChoose(action='model_car', answer='Freelander',
                                                                 model_auto_ru='FREELANDER',
                                                                 model_encar_com='프리랜더').pack()),

            types.InlineKeyboardButton(text="Sport",
                                       callback_data=ModelChoose(action='model_car', answer='Sport',
                                                                 model_auto_ru='RANGE_ROVER_SPORT',
                                                                 model_encar_com='레인지로버 스포츠').pack()),
            types.InlineKeyboardButton(text="Velar",
                                       callback_data=ModelChoose(action='model_car', answer='Velar',
                                                                 model_auto_ru='RANGE_ROVER_VELAR',
                                                                 model_encar_com='레인지로버 벨라').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Range Rover",
                                       callback_data=ModelChoose(action='model_car', answer='Range Rover',
                                                                 model_auto_ru='RANGE_ROVER',
                                                                 model_encar_com='레인지로버').pack())
        )
    elif brand_auto_ru == "LEXUS":
        kb.row(
            types.InlineKeyboardButton(text="CT",
                                       callback_data=ModelChoose(action='model_car', answer='CT',
                                                                 model_auto_ru='CT',
                                                                 model_encar_com='CT200h').pack()),
            types.InlineKeyboardButton(text="ES",
                                       callback_data=ModelChoose(action='model_car', answer='ES',
                                                                 model_auto_ru='ES',
                                                                 model_encar_com='ES').pack()),
            types.InlineKeyboardButton(text="GS",
                                       callback_data=ModelChoose(action='model_car', answer='GS',
                                                                 model_auto_ru='GS',
                                                                 model_encar_com='GS').pack()),
            types.InlineKeyboardButton(text="IS",
                                       callback_data=ModelChoose(action='model_car', answer='IS',
                                                                 model_auto_ru='IS',
                                                                 model_encar_com='IS').pack()),
            types.InlineKeyboardButton(text="LC",
                                       callback_data=ModelChoose(action='model_car', answer='LC',
                                                                 model_auto_ru='LC',
                                                                 model_encar_com='LC').pack())
        )
        kb.row(

            types.InlineKeyboardButton(text="LS",
                                       callback_data=ModelChoose(action='model_car', answer='LS',
                                                                 model_auto_ru='LS',
                                                                 model_encar_com='LS').pack()),
            types.InlineKeyboardButton(text="NX",
                                       callback_data=ModelChoose(action='model_car', answer='NX',
                                                                 model_auto_ru='NX',
                                                                 model_encar_com='NX').pack()),
            types.InlineKeyboardButton(text="RC",
                                       callback_data=ModelChoose(action='model_car', answer='RC',
                                                                 model_auto_ru='RC',
                                                                 model_encar_com='RC').pack()),
            types.InlineKeyboardButton(text="RX",
                                       callback_data=ModelChoose(action='model_car', answer='RX',
                                                                 model_auto_ru='RX',
                                                                 model_encar_com='RX').pack()),
            types.InlineKeyboardButton(text="UX",
                                       callback_data=ModelChoose(action='model_car', answer='UX',
                                                                 model_auto_ru='UX',
                                                                 model_encar_com='UX').pack())
        )
    elif brand_auto_ru == "MASERATI":
        kb.row(
            types.InlineKeyboardButton(text="Ghibli",
                                       callback_data=ModelChoose(action='model_car', answer='Ghibli',
                                                                 model_auto_ru='GHIBLI',
                                                                 model_encar_com='기블리').pack()),
            types.InlineKeyboardButton(text="GranCabrio",
                                       callback_data=ModelChoose(action='model_car', answer='GranCabrio',
                                                                 model_auto_ru='GRAN_CABRIO',
                                                                 model_encar_com='그란카브리오').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GranTurismo",
                                       callback_data=ModelChoose(action='model_car', answer='GranTurismo',
                                                                 model_auto_ru='GRAN_TURISMO',
                                                                 model_encar_com='그란투리스모').pack()),
            types.InlineKeyboardButton(text="Grecale",
                                       callback_data=ModelChoose(action='model_car', answer='Grecale',
                                                                 model_auto_ru='GRECALE',
                                                                 model_encar_com='그레칼레').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Levante",
                                       callback_data=ModelChoose(action='model_car', answer='Levante',
                                                                 model_auto_ru='LEVANTE',
                                                                 model_encar_com='르반떼').pack()),
            types.InlineKeyboardButton(text="MC20",
                                       callback_data=ModelChoose(action='model_car', answer='MC20',
                                                                 model_auto_ru='MC20',
                                                                 model_encar_com='MC20').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Quattroporte",
                                       callback_data=ModelChoose(action='model_car', answer='Quattroporte',
                                                                 model_auto_ru='QUATTROPORTE',
                                                                 model_encar_com='콰트로포르테').pack())
        )
    elif brand_auto_ru == "MERCEDES":
        kb.row(
            types.InlineKeyboardButton(text="A",
                                       callback_data=ModelChoose(action='model_car', answer='A-Класс',
                                                                 model_auto_ru='A_KLASSE',
                                                                 model_encar_com='A-클래스').pack()),
            types.InlineKeyboardButton(text="B",
                                       callback_data=ModelChoose(action='model_car', answer='B-Класс',
                                                                 model_auto_ru='B_KLASSE',
                                                                 model_encar_com='B-클래스 (MY B_)').pack()),
            types.InlineKeyboardButton(text="C",
                                       callback_data=ModelChoose(action='model_car', answer='C-Класс',
                                                                 model_auto_ru='C_KLASSE',
                                                                 model_encar_com='C-클래스').pack()),
            types.InlineKeyboardButton(text="E",
                                       callback_data=ModelChoose(action='model_car', answer='E-Класс',
                                                                 model_auto_ru='E_KLASSE',
                                                                 model_encar_com='E-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="CL",
                                       callback_data=ModelChoose(action='model_car', answer='CL-Класс',
                                                                 model_auto_ru='CL_KLASSE',
                                                                 model_encar_com='CL-클래스').pack()),
            types.InlineKeyboardButton(text="CLA",
                                       callback_data=ModelChoose(action='model_car', answer='CLA',
                                                                 model_auto_ru='CLA_KLASSE',
                                                                 model_encar_com='CLA-클래스').pack()),
            types.InlineKeyboardButton(text="CLE",
                                       callback_data=ModelChoose(action='model_car', answer='CLE',
                                                                 model_auto_ru='CLE_KLASSE',
                                                                 model_encar_com='CLE-클래스').pack()),
            types.InlineKeyboardButton(text="CLK",
                                       callback_data=ModelChoose(action='model_car', answer='CLK',
                                                                 model_auto_ru='CLK_KLASSE',
                                                                 model_encar_com='CLK-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="CLS",
                                       callback_data=ModelChoose(action='model_car', answer='CLS',
                                                                 model_auto_ru='CLS_KLASSE',
                                                                 model_encar_com='CLS-클래스').pack()),
            types.InlineKeyboardButton(text="EQA",
                                       callback_data=ModelChoose(action='model_car', answer='EQA',
                                                                 model_auto_ru='EQA',
                                                                 model_encar_com='EQA').pack()),
            types.InlineKeyboardButton(text="EQB",
                                       callback_data=ModelChoose(action='model_car', answer='EQB',
                                                                 model_auto_ru='EQB',
                                                                 model_encar_com='EQB').pack()),
            types.InlineKeyboardButton(text="EQC",
                                       callback_data=ModelChoose(action='model_car', answer='EQC',
                                                                 model_auto_ru='EQC',
                                                                 model_encar_com='EQC').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="EQE",
                                       callback_data=ModelChoose(action='model_car', answer='EQE',
                                                                 model_auto_ru='EQE',
                                                                 model_encar_com='EQE').pack()),
            types.InlineKeyboardButton(text="EQS",
                                       callback_data=ModelChoose(action='model_car', answer='EQS',
                                                                 model_auto_ru='EQS',
                                                                 model_encar_com='EQS').pack()),
            types.InlineKeyboardButton(text="G",
                                       callback_data=ModelChoose(action='model_car', answer='G-Класс',
                                                                 model_auto_ru='G_KLASSE',
                                                                 model_encar_com='G-클래스 (G바겐_)').pack()),
            types.InlineKeyboardButton(text="GL",
                                       callback_data=ModelChoose(action='model_car', answer='GL-Класс',
                                                                 model_auto_ru='GL_KLASSE',
                                                                 model_encar_com='GL-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GLA",
                                       callback_data=ModelChoose(action='model_car', answer='GLA-Класс',
                                                                 model_auto_ru='GLA_CLASS',
                                                                 model_encar_com='GLA-클래스').pack()),
            types.InlineKeyboardButton(text="GLB",
                                       callback_data=ModelChoose(action='model_car', answer='GLB-Класс',
                                                                 model_auto_ru='GLB_KLASSE',
                                                                 model_encar_com='GLB-클래스').pack()),
            types.InlineKeyboardButton(text="GLC",
                                       callback_data=ModelChoose(action='model_car', answer='GLC-Класс',
                                                                 model_auto_ru='GLC_KLASSE',
                                                                 model_encar_com='GLC-클래스').pack()),
            types.InlineKeyboardButton(text="GLE",
                                       callback_data=ModelChoose(action='model_car', answer='GLE-Класс',
                                                                 model_auto_ru='GLE_KLASSE',
                                                                 model_encar_com='GLE-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GLK",
                                       callback_data=ModelChoose(action='model_car', answer='GLK-Класс',
                                                                 model_auto_ru='GLK_KLASSE',
                                                                 model_encar_com='GLK-클래스').pack()),
            types.InlineKeyboardButton(text="GLS",
                                       callback_data=ModelChoose(action='model_car', answer='GLS-Класс',
                                                                 model_auto_ru='GLS_KLASSE',
                                                                 model_encar_com='GLS-클래스').pack()),
            types.InlineKeyboardButton(text="M",
                                       callback_data=ModelChoose(action='model_car', answer='M-Класс',
                                                                 model_auto_ru='M_KLASSE',
                                                                 model_encar_com='M-클래스').pack()),
            types.InlineKeyboardButton(text="R",
                                       callback_data=ModelChoose(action='model_car', answer='R-Класс',
                                                                 model_auto_ru='R_KLASSE',
                                                                 model_encar_com='R-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="S",
                                       callback_data=ModelChoose(action='model_car', answer='S-Класс',
                                                                 model_auto_ru='S_KLASSE',
                                                                 model_encar_com='S-클래스').pack()),
            types.InlineKeyboardButton(text="SL",
                                       callback_data=ModelChoose(action='model_car', answer='SL-Класс',
                                                                 model_auto_ru='SL_KLASSE',
                                                                 model_encar_com='SL-클래스').pack()),
            types.InlineKeyboardButton(text="SLC",
                                       callback_data=ModelChoose(action='model_car', answer='SLC-Класс',
                                                                 model_auto_ru='SLC_KLASSE',
                                                                 model_encar_com='SLC-클래스').pack()),
            types.InlineKeyboardButton(text="SLK",
                                       callback_data=ModelChoose(action='model_car', answer='SLK-Класс',
                                                                 model_auto_ru='SLK_KLASSE',
                                                                 model_encar_com='SLK-클래스').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="SLS AMG",
                                       callback_data=ModelChoose(action='model_car', answer='SLS AMG',
                                                                 model_auto_ru='SLS_AMG',
                                                                 model_encar_com='SLS AMG').pack()),
            types.InlineKeyboardButton(text="AMG GT",
                                       callback_data=ModelChoose(action='model_car', answer='AMG GT',
                                                                 model_auto_ru='AMG_GT',
                                                                 model_encar_com='AMG GT').pack()),
            types.InlineKeyboardButton(text="V",
                                       callback_data=ModelChoose(action='model_car', answer='V-Класс',
                                                                 model_auto_ru='V_KLASSE',
                                                                 model_encar_com='V-클래스').pack())
        )
    elif brand_auto_ru == "MINI":
        kb.row(
            types.InlineKeyboardButton(text="Clubman",
                                       callback_data=ModelChoose(action='model_car', answer='Clubman',
                                                                 model_auto_ru='CLUBMAN',
                                                                 model_encar_com='클럽맨').pack()),
            types.InlineKeyboardButton(text="Countryman",
                                       callback_data=ModelChoose(action='model_car', answer='Countryman',
                                                                 model_auto_ru='COUNTRYMAN',
                                                                 model_encar_com='컨트리맨').pack()),
            types.InlineKeyboardButton(text="Coupe",
                                       callback_data=ModelChoose(action='model_car', answer='Coupe',
                                                                 model_auto_ru='COUPE',
                                                                 model_encar_com='쿠페').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Paceman",
                                       callback_data=ModelChoose(action='model_car', answer='Paceman',
                                                                 model_auto_ru='PACEMAN',
                                                                 model_encar_com='페이스맨').pack()),
            types.InlineKeyboardButton(text="Roadster",
                                       callback_data=ModelChoose(action='model_car', answer='Roadster',
                                                                 model_auto_ru='ROADSTER',
                                                                 model_encar_com='로드스터').pack())
        )

    elif brand_auto_ru == "NISSAN":
        kb.row(
            types.InlineKeyboardButton(text="350Z",
                                       callback_data=ModelChoose(action='model_car', answer='350Z',
                                                                 model_auto_ru='350Z',
                                                                 model_encar_com='350Z').pack()),
            types.InlineKeyboardButton(text="370Z",
                                       callback_data=ModelChoose(action='model_car', answer='370Z',
                                                                 model_auto_ru='370Z',
                                                                 model_encar_com='370Z').pack()),
            types.InlineKeyboardButton(text="Altima",
                                       callback_data=ModelChoose(action='model_car', answer='Altima',
                                                                 model_auto_ru='ALTIMA',
                                                                 model_encar_com='알티마').pack())
        )
        kb.row(

            types.InlineKeyboardButton(text="Cube",
                                       callback_data=ModelChoose(action='model_car', answer='Cube',
                                                                 model_auto_ru='CUBE',
                                                                 model_encar_com='큐브').pack()),
            types.InlineKeyboardButton(text="GT-R",
                                       callback_data=ModelChoose(action='model_car', answer='GT-R',
                                                                 model_auto_ru='GT_R',
                                                                 model_encar_com='GT-R').pack()),
            types.InlineKeyboardButton(text="Juke",
                                       callback_data=ModelChoose(action='model_car', answer='Juke',
                                                                 model_auto_ru='JUKE',
                                                                 model_encar_com='쥬크').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Leaf",
                                       callback_data=ModelChoose(action='model_car', answer='Leaf',
                                                                 model_auto_ru='LEAF',
                                                                 model_encar_com='리프').pack()),
            types.InlineKeyboardButton(text="Maxima",
                                       callback_data=ModelChoose(action='model_car', answer='Maxima',
                                                                 model_auto_ru='MAXIMA',
                                                                 model_encar_com='맥시마').pack()),
            types.InlineKeyboardButton(text="Murano",
                                       callback_data=ModelChoose(action='model_car', answer='Murano',
                                                                 model_auto_ru='MURANO',
                                                                 model_encar_com='무라노').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Pathfinder",
                                       callback_data=ModelChoose(action='model_car', answer='Pathfinder',
                                                                 model_auto_ru='PATHFINDER',
                                                                 model_encar_com='패스파인더').pack()),
            types.InlineKeyboardButton(text="Skyline",
                                       callback_data=ModelChoose(action='model_car', answer='Skyline',
                                                                 model_auto_ru='SKYLINE',
                                                                 model_encar_com='스카이라인').pack()),
            types.InlineKeyboardButton(text="X-Trail",
                                       callback_data=ModelChoose(action='model_car', answer='X-Trail',
                                                                 model_auto_ru='X_TRAIL',
                                                                 model_encar_com='엑스트레일').pack())
        )
    elif brand_auto_ru == "PORSCHE":
        kb.row(
            types.InlineKeyboardButton(text="911",
                                       callback_data=ModelChoose(action='model_car', answer='911',
                                                                 model_auto_ru='911',
                                                                 model_encar_com='911').pack()),
            types.InlineKeyboardButton(text="Boxster",
                                       callback_data=ModelChoose(action='model_car', answer='Boxster',
                                                                 model_auto_ru='BOXSTER',
                                                                 model_encar_com='박스터').pack()),
            types.InlineKeyboardButton(text="Cayenne",
                                       callback_data=ModelChoose(action='model_car', answer='Cayenne',
                                                                 model_auto_ru='CAYENNE',
                                                                 model_encar_com='카이엔').pack()),
            types.InlineKeyboardButton(text="Cayman",
                                       callback_data=ModelChoose(action='model_car', answer='Cayman',
                                                                 model_auto_ru='CAYMAN',
                                                                 model_encar_com='카이맨').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Macan",
                                       callback_data=ModelChoose(action='model_car', answer='Macan',
                                                                 model_auto_ru='MACAN',
                                                                 model_encar_com='마칸').pack()),
            types.InlineKeyboardButton(text="Panamera",
                                       callback_data=ModelChoose(action='model_car', answer='Panamera',
                                                                 model_auto_ru='PANAMERA',
                                                                 model_encar_com='파나메라').pack()),
            types.InlineKeyboardButton(text="Taycan",
                                       callback_data=ModelChoose(action='model_car', answer='Taycan',
                                                                 model_auto_ru='TAYCAN',
                                                                 model_encar_com='타이칸').pack())
        )
    elif brand_auto_ru == "ROLLS_ROYCE":
        kb.row(
            types.InlineKeyboardButton(text="Cullinan",
                                       callback_data=ModelChoose(action='model_car', answer='Cullinan',
                                                                 model_auto_ru='CULLINAN',
                                                                 model_encar_com='컬리넌').pack()),
            types.InlineKeyboardButton(text="Dawn",
                                       callback_data=ModelChoose(action='model_car', answer='Dawn',
                                                                 model_auto_ru='DAWN',
                                                                 model_encar_com='던').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Ghost",
                                       callback_data=ModelChoose(action='model_car', answer='Ghost',
                                                                 model_auto_ru='GHOST',
                                                                 model_encar_com='고스트').pack()),
            types.InlineKeyboardButton(text="Phantom",
                                       callback_data=ModelChoose(action='model_car', answer='Phantom',
                                                                 model_auto_ru='PHANTOM',
                                                                 model_encar_com='팬텀').pack())
        )
    elif brand_auto_ru == "TESLA":
        kb.row(
            types.InlineKeyboardButton(text="Model 3",
                                       callback_data=ModelChoose(action='model_car', answer='Model 3',
                                                                 model_auto_ru='MODEL_3',
                                                                 model_encar_com='모델 3').pack()),
            types.InlineKeyboardButton(text="Model S",
                                       callback_data=ModelChoose(action='model_car', answer='Model S',
                                                                 model_auto_ru='MODEL_S',
                                                                 model_encar_com='모델 S').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Model X",
                                       callback_data=ModelChoose(action='model_car', answer='Model X',
                                                                 model_auto_ru='MODEL_X',
                                                                 model_encar_com='모델 X').pack()),
            types.InlineKeyboardButton(text="Model Y",
                                       callback_data=ModelChoose(action='model_car', answer='Model Y',
                                                                 model_auto_ru='MODEL_Y',
                                                                 model_encar_com='모델 Y').pack())
        )
    elif brand_auto_ru == "TOYOTA":
        kb.row(
            types.InlineKeyboardButton(text="Avalon",
                                       callback_data=ModelChoose(action='model_car', answer='Avalon',
                                                                 model_auto_ru='AVALON',
                                                                 model_encar_com='아발론').pack()),
            types.InlineKeyboardButton(text="Camry",
                                       callback_data=ModelChoose(action='model_car', answer='Camry',
                                                                 model_auto_ru='CAMRY',
                                                                 model_encar_com='캠리').pack()),
            types.InlineKeyboardButton(text="FJ Cruiser",
                                       callback_data=ModelChoose(action='model_car', answer='FJ Cruiser',
                                                                 model_auto_ru='FJ_CRUISER',
                                                                 model_encar_com='FJ 크루져').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="GR86",
                                       callback_data=ModelChoose(action='model_car', answer='GR86',
                                                                 model_auto_ru='GR86',
                                                                 model_encar_com='86').pack()),
            types.InlineKeyboardButton(text="Prius",
                                       callback_data=ModelChoose(action='model_car', answer='Prius',
                                                                 model_auto_ru='PRIUS',
                                                                 model_encar_com='프리우스').pack()),
            types.InlineKeyboardButton(text="RAV4",
                                       callback_data=ModelChoose(action='model_car', answer='RAV4',
                                                                 model_auto_ru='RAV_4',
                                                                 model_encar_com='RAV4').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="4Runner",
                                       callback_data=ModelChoose(action='model_car', answer='4Runner',
                                                                 model_auto_ru='4RUNNER',
                                                                 model_encar_com='4Runner').pack()),
            types.InlineKeyboardButton(text="Sienna",
                                       callback_data=ModelChoose(action='model_car', answer='Sienna',
                                                                 model_auto_ru='SIENNA',
                                                                 model_encar_com='시에나').pack()),
            types.InlineKeyboardButton(text="Supra",
                                       callback_data=ModelChoose(action='model_car', answer='Supra',
                                                                 model_auto_ru='SUPRA',
                                                                 model_encar_com='수프라').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Tacoma",
                                       callback_data=ModelChoose(action='model_car', answer='Tacoma',
                                                                 model_auto_ru='TACOMA',
                                                                 model_encar_com='타코마').pack()),
            types.InlineKeyboardButton(text="Tundra",
                                       callback_data=ModelChoose(action='model_car', answer='Tundra',
                                                                 model_auto_ru='TUNDRA',
                                                                 model_encar_com='툰드라').pack()),

            types.InlineKeyboardButton(text="Venza",
                                       callback_data=ModelChoose(action='model_car', answer='Venza',
                                                                 model_auto_ru='VENZA',
                                                                 model_encar_com='벤자').pack())
        )
    elif brand_auto_ru == "VOLKSWAGEN":
        kb.row(
            types.InlineKeyboardButton(text="Arteon",
                                       callback_data=ModelChoose(action='model_car', answer='Arteon',
                                                                 model_auto_ru='ARTEON',
                                                                 model_encar_com='아테온').pack()),
            types.InlineKeyboardButton(text="Beetle",
                                       callback_data=ModelChoose(action='model_car', answer='Beetle',
                                                                 model_auto_ru='BEETLE',
                                                                 model_encar_com='비틀').pack()),
            types.InlineKeyboardButton(text="Eos",
                                       callback_data=ModelChoose(action='model_car', answer='Eos',
                                                                 model_auto_ru='EOS',
                                                                 model_encar_com='EOS').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Golf",
                                       callback_data=ModelChoose(action='model_car', answer='Golf',
                                                                 model_auto_ru='GOLF',
                                                                 model_encar_com='골프').pack()),
            types.InlineKeyboardButton(text="ID.4",
                                       callback_data=ModelChoose(action='model_car', answer='ID.4',
                                                                 model_auto_ru='ID4',
                                                                 model_encar_com='ID_.4').pack()),
            types.InlineKeyboardButton(text="Jetta",
                                       callback_data=ModelChoose(action='model_car', answer='Jetta',
                                                                 model_auto_ru='JETTA',
                                                                 model_encar_com='제타').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Passat",
                                       callback_data=ModelChoose(action='model_car', answer='Passat',
                                                                 model_auto_ru='PASSAT',
                                                                 model_encar_com='파사트').pack()),
            types.InlineKeyboardButton(text="Phaeton",
                                       callback_data=ModelChoose(action='model_car', answer='Phaeton',
                                                                 model_auto_ru='PHAETON',
                                                                 model_encar_com='페이톤').pack()),
            types.InlineKeyboardButton(text="Polo",
                                       callback_data=ModelChoose(action='model_car', answer='Polo',
                                                                 model_auto_ru='POLO',
                                                                 model_encar_com='폴로').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="Scirocco",
                                       callback_data=ModelChoose(action='model_car', answer='Scirocco',
                                                                 model_auto_ru='SCIROCCO',
                                                                 model_encar_com='시로코').pack()),
            types.InlineKeyboardButton(text="Tiguan",
                                       callback_data=ModelChoose(action='model_car', answer='Tiguan',
                                                                 model_auto_ru='TIGUAN',
                                                                 model_encar_com='티구안').pack()),

            types.InlineKeyboardButton(text="Touareg",
                                       callback_data=ModelChoose(action='model_car', answer='Touareg',
                                                                 model_auto_ru='TOUAREG',
                                                                 model_encar_com='투아렉').pack()),
            types.InlineKeyboardButton(text="T-Roc",
                                       callback_data=ModelChoose(action='model_car', answer='T-Roc',
                                                                 model_auto_ru='T_ROC',
                                                                 model_encar_com='티록').pack()),

        )
    elif brand_auto_ru == "VOLVO":
        kb.row(
            types.InlineKeyboardButton(text="C30",
                                       callback_data=ModelChoose(action='model_car', answer='C30',
                                                                 model_auto_ru='C30',
                                                                 model_encar_com='C30').pack()),
            types.InlineKeyboardButton(text="C40",
                                       callback_data=ModelChoose(action='model_car', answer='C40',
                                                                 model_auto_ru='C40',
                                                                 model_encar_com='C40').pack()),
            types.InlineKeyboardButton(text="S40",
                                       callback_data=ModelChoose(action='model_car', answer='S40',
                                                                 model_auto_ru='S40',
                                                                 model_encar_com='S40').pack()),
            types.InlineKeyboardButton(text="S60",
                                       callback_data=ModelChoose(action='model_car', answer='S60',
                                                                 model_auto_ru='S60',
                                                                 model_encar_com='S60').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="S70",
                                       callback_data=ModelChoose(action='model_car', answer='S70',
                                                                 model_auto_ru='S70',
                                                                 model_encar_com='S70').pack()),
            types.InlineKeyboardButton(text="S80",
                                       callback_data=ModelChoose(action='model_car', answer='S80',
                                                                 model_auto_ru='S80',
                                                                 model_encar_com='S80').pack()),
            types.InlineKeyboardButton(text="S90",
                                       callback_data=ModelChoose(action='model_car', answer='S90',
                                                                 model_auto_ru='S90',
                                                                 model_encar_com='S90').pack()),
            types.InlineKeyboardButton(text="V40",
                                       callback_data=ModelChoose(action='model_car', answer='V40',
                                                                 model_auto_ru='V40',
                                                                 model_encar_com='V40').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="V50",
                                       callback_data=ModelChoose(action='model_car', answer='V50',
                                                                 model_auto_ru='V50',
                                                                 model_encar_com='V50').pack()),
            types.InlineKeyboardButton(text="V60",
                                       callback_data=ModelChoose(action='model_car', answer='V60',
                                                                 model_auto_ru='V60',
                                                                 model_encar_com='V60').pack()),
            types.InlineKeyboardButton(text="V70",
                                       callback_data=ModelChoose(action='model_car', answer='V70',
                                                                 model_auto_ru='V70',
                                                                 model_encar_com='V70').pack()),
            types.InlineKeyboardButton(text="V90",
                                       callback_data=ModelChoose(action='model_car', answer='V90',
                                                                 model_auto_ru='V90',
                                                                 model_encar_com='V90').pack())
        )
        kb.row(
            types.InlineKeyboardButton(text="XC40",
                                       callback_data=ModelChoose(action='model_car', answer='XC40',
                                                                 model_auto_ru='XC40',
                                                                 model_encar_com='XC40').pack()),
            types.InlineKeyboardButton(text="XC60",
                                       callback_data=ModelChoose(action='model_car', answer='XC60',
                                                                 model_auto_ru='XC60',
                                                                 model_encar_com='XC60').pack()),
            types.InlineKeyboardButton(text="XC70",
                                       callback_data=ModelChoose(action='model_car', answer='XC70',
                                                                 model_auto_ru='XC70',
                                                                 model_encar_com='XC70').pack()),
            types.InlineKeyboardButton(text="XC90",
                                       callback_data=ModelChoose(action='model_car', answer='XC90',
                                                                 model_auto_ru='XC90',
                                                                 model_encar_com='XC90').pack())
        )
    return kb.as_markup()
