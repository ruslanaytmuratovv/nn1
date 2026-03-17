import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg:Message):
    await msg.answer('salem hammme')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


