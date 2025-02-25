from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Create buttons for main menu
button_fill_checklist = KeyboardButton(text="🧹Заполнить чек-лист")
button_check_checklist = KeyboardButton(text="🔍Проверить чек-лист")
button_cases_menu = KeyboardButton(text="📝Открыть меню кейсов")
button_birthdays = KeyboardButton(text="🎉Напомнить дни рождения")

# Create keyboard
keyboard_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [button_fill_checklist, button_check_checklist],
        [button_birthdays],
        [button_cases_menu]
    ],
    resize_keyboard=True
)
