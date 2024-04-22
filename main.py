import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
from handlers import start_handler, car_params_handler
from handlers.start_handler import router

# bot = Bot(token=os.getenv("TOKEN"))
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

 
async def main():
    dp.include_router(start_handler.router)
    dp.include_router(car_params_handler.router)

    # Start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# ToDo: add token in env
# ToDo: write xml for every function
