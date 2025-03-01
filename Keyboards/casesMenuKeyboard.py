from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Create buttons for cases menu
button_new_case = KeyboardButton(text="⚡Новый кейс")
button_active_cases = KeyboardButton(text="🟡Активные кейсы")
button_closed_cases = KeyboardButton(text="✅Закрытые кейсы")
button_back_to_main_menu = KeyboardButton(text="⬅️В главное меню")

# Create cases menu keyboard
keyboard_cases_menu = ReplyKeyboardMarkup(
    keyboard=[
        [button_new_case, button_active_cases],
        [button_closed_cases, button_back_to_main_menu]
    ],
    resize_keyboard=True
)
