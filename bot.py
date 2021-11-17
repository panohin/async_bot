#!venv/bin/python3.9
import logging
from aiogram import Bot, Dispatcher, executor, types
import config


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# /test1
async def cmd_test1(message: types.Message):
    await message.reply("Test1")

dp.register_message_handler(cmd_test1, commands="test1")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

