import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router

# bot = Bot(token=os.getenv("TOKEN"))
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

 
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# ToDo: add token in env
# ToDo: write xml for every function
