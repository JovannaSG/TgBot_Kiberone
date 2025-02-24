from aiogram import Router, types
from aiogram.filters import Command

main_router = Router()


@main_router.message(Command("start", prefix="/"))
async def start_command(message: types.Message):
    await message.answer("Hello!")
