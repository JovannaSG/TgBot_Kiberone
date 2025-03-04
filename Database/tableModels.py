# from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class photoTable(Base):
    __tablename__ = "photo"

    photo_id: Mapped[int] = mapped_column(primary_key=True)
    photo_path: Mapped[str] = mapped_column(String(80))

    def __repr__(self) -> str:
        return f"photo(photo_id={self.photo_id}, " \
            + f"photo_path={self.photo_path})"


class foodTable(Base):
    __tablename__ = "food"

    food_name_id: Mapped[int] = mapped_column(primary_key=True)
    food_name: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"food(food_name_id={self.food_name_id}, " \
            + f"food_name={self.food_name})"


class foodAmountTable(Base):
    __tablename__ = "food_amount"

    food_amount_id: Mapped[int] = mapped_column(primary_key=True)
    food_name_id: Mapped[int] = mapped_column(ForeignKey("food.food_name_id"))
    food_amount: Mapped[int]

    def __repr__(self) -> str:
        return f"food_amount(food_amount_id={self.food_amount_id}, " \
            + f"food_name_id={self.food_name_id}, " \
            + f"food_amount={self.food_amount})"


class userRoleTable(Base):
    __tablename__ = "user_role"

    user_role_id: Mapped[int] = mapped_column(primary_key=True)
    user_role_name: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"user_role(user_role_id={self.user_role_id}, " \
            + f"user_role_name={self.user_role_name})"


class employeeTable(Base):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    employee_full_name: Mapped[str] = mapped_column(String(40))
    employee_telegram_id: Mapped[str] = mapped_column(String(80))
    user_role_id: Mapped[int] = mapped_column(ForeignKey("user_role.user_role_id"))

    def __repr__(self) -> str:
        return f"employee(employee_id={self.employee_id}, " \
            + f"employee_full_name={self.employee_full_name}, " \
            + f"employee_telegram_id={self.employee_telegram_id}, " \
            + f"user_role_id={self.user_role_id})"


class residentBirthdayTable(Base):
    __tablename__ = "resident_birthday"

    resident_birthday_id: Mapped[int] = mapped_column(primary_key=True)
    resident_group: Mapped[str] = mapped_column(String(30))
    resident_full_name: Mapped[str] = mapped_column(String(40))
    tutor_id: Mapped[int] = mapped_column(ForeignKey("employee.employee_id"))
    assistant_id: Mapped[int] = mapped_column(ForeignKey("employee.employee_id"))
    resident_birthday_date: Mapped[str] = mapped_column(String(12))

    def __repr__(self) -> str:
        return f"resident_birthday(resident_birthday_id={self.resident_birthday_id}, " \
            + f"resident_group={self.resident_group}, " \
            + f"resident_full_name={self.resident_full_name}, " \
            + f"tutor_id={self.tutor_id}, " \
            + f"assistant_id={self.assistant_id}, " \
            + f"resident_birthday_date={self.resident_birthday_date})"


class checklistTable(Base):
    __tablename__ = "checklist"

    checklist_id: Mapped[int] = mapped_column(primary_key=True)
    antiseptic: Mapped[str] = mapped_column(String(20))
    bars_trial_lesson: Mapped[str] = mapped_column(String(20))
    bottles_of_water: Mapped[str] = mapped_column(String(20))
    cleaning_products: Mapped[str] = mapped_column(String(20))
    cofee: Mapped[str] = mapped_column(String(20))
    cups: Mapped[str] = mapped_column(String(20))
    date: Mapped[str] = mapped_column(String(12))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.employee_id"))
    kiberones: Mapped[str] = mapped_column(String(20))
    markers: Mapped[str] = mapped_column(String(20))
    office_paper: Mapped[str] = mapped_column(String(20))
    pens: Mapped[str] = mapped_column(String(20))
    rags: Mapped[str] = mapped_column(String(20))
    soap: Mapped[str] = mapped_column(String(20))
    tea_bags: Mapped[str] = mapped_column(String(20))
    toilet_paper: Mapped[str] = mapped_column(String(20))
    napkins: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"checklist(checklist_id={self.checklist_id}, " \
            + f"antiseptic={self.antiseptic}, " \
            + f"bars_trial_lesson={self.bars_trial_lesson}, " \
            + f"bottles_of_water={self.bottles_of_water}, " \
            + f"cleaning_products={self.cleaning_products}, " \
            + f"cofee={self.cofee}, " \
            + f"cups={self.cups}, " \
            + f"date={self.date}, " \
            + f"employee_id={self.employee_id}, " \
            + f"kiberones={self.kiberones}, " \
            + f"markers={self.markers}, " \
            + f"office_paper={self.office_paper}, " \
            + f"pens={self.pens}, " \
            + f"rags={self.rags}, " \
            + f"soap={self.soap}, " \
            + f"tea_bags={self.tea_bags}, " \
            + f"toilet_paper={self.toilet_paper})"


class locationTable(Base):
    __tablename__ = "location"

    location_id: Mapped[int] = mapped_column(primary_key=True)
    location_name: Mapped[str] = mapped_column(String(20))
    photo_id: Mapped[int] = mapped_column(ForeignKey("photo.photo_id"))
    food_amount_id: Mapped[int] = mapped_column(ForeignKey("food_amount.food_amount_id"))
    checklist_id: Mapped[int] = mapped_column(ForeignKey("checklist.checklist_id"))

    def __repr__(self) -> str:
        return f"location(location_id={self.location_id}, " \
            + f"location_name={self.location_name}, " \
            + f"photo_id={self.photo_id}, " \
            + f"food_amount_id={self.food_amount_id}, " \
            + f"checklist_id={self.checklist_id})"
