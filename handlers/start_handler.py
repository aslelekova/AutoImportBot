# start_handler.py
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards.marks_keyboard import brand_choose

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Handler for the /start command.

    :param message: The message triggering the command.
    """
    await message.answer(f'✋ Приветствую, {message.from_user.username}!'
                         f'\n\nЯ Telegram-бот для расчета стоимости корейских автомобилей, я помогу '
                         f'рассчитать цену и другие детали по доставке машины в РФ.\n\n'
                         f'💰 Также я предоставлю информацию по похожим автомобилям в России для сравнения.\n\n🚘 '
                         f'Какая марка вас интересует?', reply_markup=brand_choose())


@router.message(Command("help"))
async def handle_help(message: types.Message):
    """
    Handle the /help command to provide information about available commands and how to use the bot.

    :param message: The message object.
    :return: None
    """
    await message.answer(text="Привет! Я бот, который поможет вам найти подходящий автомобиль.\n\n"
                              "Чтобы начать, вы можете использовать следующие команды:\n"
                              "/start - начать диалог с ботом\n"
                              "/help - получить справку о доступных командах\n\n"
                              "Если у вас возникли вопросы или вы нашли для себя подходящий автомобиль, "
                              "пишите удобным способом!\n\n📲+7 (495) 844-88-08\n✉️Телеграм: @PRIDECARSAUTO\n📁WhatsApp: "
                              "wa.me/79802120669\n🔗Сайт: https://pride-cars.com/"
)
