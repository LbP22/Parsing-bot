import asyncio

from aiogram import Bot, Dispatcher, executor
from bot_config import TOKEN

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from bot_handlers import dp, start_notification
    executor.start_polling(dp, on_startup=start_notification)
