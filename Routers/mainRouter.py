from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from Keyboards.mainMenuKeyboard import keyboard_main_menu
from Keyboards.locationsMenuKeyboard import keyboard_locations_menu

main_router = Router(name="main_router")


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


@main_router.message(F.text == "🎉Напомнить дни рождения")
async def remind_birthdays(message: types.Message):
    await message.answer(
        text="Напоминаю про др резидентов",
        reply_markup=keyboard_locations_menu
    )


@main_router.message(F.text == "⬅️В главное меню")
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await message.answer(
        text="Меню действий",
        reply_markup=keyboard_main_menu
    )
    await state.set_state(default_state)
