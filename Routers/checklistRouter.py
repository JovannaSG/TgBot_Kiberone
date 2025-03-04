from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup

from sqlalchemy import select

from Database.database import async_session
from Database.tableModels import checklistTable, foodAmountTable
from Keyboards.locationsMenuKeyboard import (
    keyboard_locations_menu,
    keyboard_back_menu
)


# locations maybe can be moved in filter
locations = [b[0].text for b in keyboard_locations_menu.keyboard]
print(locations)
date = "25-02-2025"
time = "20:12"

checklist_router = Router(name="locations_router")


class FSMFillCheklist(StatesGroup):
    # Creating instances of the State class, sequentially
    # listing the possible states it will be in
    # bot at different moments of user interaction
    location_choice_state = State()
    upload_photo_state = State()
    fill_info_state = State()


@checklist_router.message(
    F.text == "🔍Проверить чек-лист",
    StateFilter(default_state)
)
async def start_check_checklist(message: types.Message):
    await message.answer(
        text="Выберите локацию, для которой хотите посмотреть чек-лист:",
        reply_markup=keyboard_locations_menu
    )

    async with async_session() as session:
        stmt = select(foodAmountTable.food_amount).where(
            foodAmountTable.food_amount_id == 1
        )
        print(stmt)
        result = await session.execute(stmt)
        food_result = result.scalars().all()
        print(food_result)

    async with async_session() as session:
        stmt = select(checklistTable)
        print(stmt)
        result = await session.execute(stmt)
        consumables_result = result.scalars().all()
        print(consumables_result)

    await message.reply(
        f"Остатки продуктов: {food_result[0]}\n\n" \
        + "Остатки расходников\n" \
        + f"Вода: {consumables_result[0].bottles_of_water}\n" \
        + f"Бумага туалетная: {consumables_result[0].toilet_paper}\n" \
        + f"Салфетки: {consumables_result[0].napkins}\n" \
        + f"Антисептик: {consumables_result[0].antiseptic}\n" \
        + f"Бумага офисная: {consumables_result[0].office_paper}\n" \
        + f"Мыло: {consumables_result[0].soap}\n" \
        + f"Тряпки: {consumables_result[0].rags}\n" \
        + f"Средства для уборки: {consumables_result[0].cleaning_products}\n" \
        + f"Стаканчики: {consumables_result[0].cups}\n" \
        + f"Чай: {consumables_result[0].tea_bags}\n" \
        + f"Карандаши/фломастеры: {consumables_result[0].pens}\n" \
        + f"Маркеры: {consumables_result[0].markers}\n" \
        + f"Кофе: {consumables_result[0].cofee}\n" \
        + f"Батончики для пробника: {consumables_result[0].bars_trial_lesson}" \
    )


@checklist_router.message(F.text == "🧹Заполнить чек-лист")
async def start_fill_checklist(message: types.Message, state: FSMContext):
    await message.answer(
        text=f"🧹Последний раз чек-лист для {message.text} " + \
            f"был заполнен {date} {time}"
    )
    await message.answer(
        text="Выберите локацию, для которой хотите заполнить чек-лист:",
        reply_markup=keyboard_locations_menu
    )
    await state.set_state(FSMFillCheklist.location_choice_state)


@checklist_router.message(
    F.text.in_(locations),
    StateFilter(FSMFillCheklist.location_choice_state)
)
async def process_location(message: types.Message, state: FSMContext):
    await message.answer(
        text="📷Пожалуйста, отправьте фото состояния локации." +
            "Вы можете отправить несколько фото.",
        reply_markup=keyboard_back_menu
    )
    await state.set_state(FSMFillCheklist.upload_photo_state)


@checklist_router.message(StateFilter(FSMFillCheklist.location_choice_state))
async def warning_not_location(message: types.Message):
    await message.answer(
        text="Пожалуйста, на этом шаге выберите локацию из списка в меню"
    )


# This handler will be triggered if a photo is sent
# and bring it to a state of fill info
@checklist_router.message(
    F.photo[-1].as_("largest_photo"),
    StateFilter(FSMFillCheklist.upload_photo_state)
)
async def process_photo(
    message: types.Message,
    state: FSMContext,
    largest_photo: types.PhotoSize
):
    # Saving the photo data (file_unique_id and file_id) to the storage
    # by the keys "photo_unique_id" and "photo_id"
    # def send info in bd(): pass
    await message.answer(text="Теперь отправьте такую-то информацию")
    # Setting the waiting state for the choice of education
    await state.set_state(FSMFillCheklist.fill_info_state)


# This handler will be triggered if while sending a photo
# something incorrect will be entered/sent
@checklist_router.message(StateFilter(FSMFillCheklist.upload_photo_state))
async def warning_not_photo(message: types.Message):
    await message.answer(
        text="Пожалуйста, на этом шаге отправьте фото локации"
    )


@checklist_router.message(
    F.text,
    StateFilter(FSMFillCheklist.fill_info_state)
)
async def process_location(message: types.Message, state: FSMContext):
    await message.answer(
        text="Пока что конец FSM для заполнения чек-листа",
        reply_markup=keyboard_back_menu
    )
    await state.set_state(default_state)
