from typing import Optional
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=5, max_length=40)
    phone: str = Field(regex=r"^[0-9]{10}$", min_length=11, max_length=11)
    email: str = Field(min_length=6, max_length=40)


class UserCreate(UserBase):
    password: str = Field(min_length=5, max_length=40)


class Users(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str = Field(min_length=5, max_length=40)
