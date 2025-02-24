import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import bot_config
from Routers.mainRouter import main_router


# We turn on logging so as not to miss important messages
logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=bot_config.bot_token.get_secret_value(),
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher()


# start polling and new updates
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
