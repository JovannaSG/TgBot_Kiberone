from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Create buttons for main menu
# МТЦ Новый
button_ITC_New = KeyboardButton(text="МТЦ Новый")
# 2ЖД
button_2RW = KeyboardButton(text="2ЖД")
# Солнечный 1
button_Sun1 = KeyboardButton(text="Солнечный 1")
# Солнечный 1
button_Sun2 = KeyboardButton(text="Солнечный 2")
# НЛО
button_NLO = KeyboardButton(text="НЛО")
# Back to main menu
button_back_to_main_menu = KeyboardButton(text="⬅️В главное меню")

# Create keyboard
keyboard_locations_menu = ReplyKeyboardMarkup(
    keyboard=[
        [button_ITC_New],
        [button_2RW],
        [button_Sun1],
        [button_Sun2],
        [button_NLO],
        [button_back_to_main_menu]
    ],
    resize_keyboard=True
)

keyboard_back_menu = ReplyKeyboardMarkup(
    keyboard=[[button_back_to_main_menu]],
    resize_keyboard=True
)
