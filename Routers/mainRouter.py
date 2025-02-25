from aiogram import Router, types, F
from aiogram.filters import Command

from Keyboards.mainMenuKeyboard import keyboard_main_menu


main_router = Router()


@main_router.message(Command("start", prefix="/"))
async def start_command(message: types.Message):
    await message.answer(
        text="Добро пожаловать, выберите действие из главного меню",
        reply_markup=keyboard_main_menu
    )


@main_router.message(Command("help", prefix="/"))
async def help_command(message: types.Message):
    await message.answer(
        text="Справка по боту"
    )
