import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
# from aiogram.fsm.storage.memory import MemoryStorage

from config import bot_config
from Routers.mainRouter import main_router
from Routers.casesRouter import cases_router
from Routers.checklistRouter import checklist_router


# We turn on logging so as not to miss important messages
logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=bot_config.bot_token.get_secret_value(),
    default=DefaultBotProperties(parse_mode="HTML")
)
# storage = MemoryStorage()
# storage=storage
dp = Dispatcher()


async def set_main_commands(bot: Bot):
    # Creating a list with commands and their descriptions
    main_commands = [
        BotCommand(
            command="/start",
            description="Запуск бота"
        ),
        BotCommand(
            command="/help",
            description="Справка по работе бота"
        )
    ]
    await bot.set_my_commands(main_commands)


# start polling and new updates
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # add commands on menu
    dp.startup.register(set_main_commands)
    dp.include_routers(
        main_router,
        cases_router,
        checklist_router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
