# main.py
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
from handlers import start_handler, car_params_handler


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# bot = Bot(token=os.getenv("TOKEN"))
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


async def main():
    try:
        dp.include_router(start_handler.router)
        dp.include_router(car_params_handler.router)

        # Start the bot
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception("An error occurred while running the bot: %s", e)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception("An error occurred in the main loop: %s", e)

# ToDo: add token in env
