from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum

# Валидация пола
class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

# ORM модель с валидацией pydantic
class users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    date_of_birth: date
    gender: Gender


