from aiogram import Router, types, F
from aiogram.filters import Command

from Keyboards.locationsMenuKeyboard import (
    keyboard_locations_menu,
    keyboard_back_menu
)

locations_router = Router()


@locations_router.message(F.text == "🧹Заполнить чек-лист")
async def open_locations_menu(message: types.Message):
    await message.answer(
        text="Выберите локацию, для которой хотите заполнить чек-лист:",
        reply_markup=keyboard_locations_menu
    )


# locations maybe can be moved in filter
locations = [b[0].text for b in keyboard_locations_menu.keyboard]
print(locations)
date = "25-02-2025"
time = "20:12"

@locations_router.message(F.text.in_(locations))
async def photo_request(message: types.Message):
    await message.answer(
        text=f"🧹Последний раз чек-лист для {message.text} " + \
            f"был заполнен {date} {time}"
    )
    await message.answer(
        text="📷Пожалуйста, отправьте фото состояния локации. Вы можете отправить несколько фото.",
        reply_markup=keyboard_back_menu
    )
