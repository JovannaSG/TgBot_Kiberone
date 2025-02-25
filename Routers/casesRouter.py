from aiogram import Router, types, F

from Keyboards.mainMenuKeyboard import keyboard_main_menu
from Keyboards.casesMenuKeyboard import keyboard_cases_menu

cases_router = Router()


# Open cases menu
@cases_router.message(F.text == "📝Открыть меню кейсов")
async def open_menu_cases(message: types.Message):
    await message.answer(
        text="Меню кейсов",
        reply_markup=keyboard_cases_menu
    )


# Back to main menu
@cases_router.message(F.text == "🔙В главное меню")
async def back_to_main_menu(message: types.Message):
    await message.answer(
        text="Меню действий",
        reply_markup=keyboard_main_menu
    )
