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

@dp.message(Command('help'))
async def help(msg:Message):
    await msg.answer('ne jardem kerek')
#2
@dp.message(Command('contact'))
async def help(msg:Message):
    await msg.answer('admin')
#3
@dp.message(Command('admin'))
async def help(msg:Message):
    await msg.answer('joq')
#4
@dp.message(Command('donate'))
async def help(msg:Message):
    await msg.answer('aksha')
#5
@dp.message(Command('money'))
async def help(msg:Message):
    await msg.answer('joq')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


