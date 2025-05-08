from typing import Optional
from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime


class UserBase(SQLModel):
    # username: str = Field(min_length=3, max_length=20)
    # password: str = Field(min_length=5, max_length=40)
    # phone: str = Field(regex=r"^[0-9]{10}$", min_length=11, max_length=11)
    # email: str = Field(min_length=6, max_length=40)
    user_id: int = Field(default=None, primary_key=True)
    username: str = Field()
    password: str = Field()
    phone: str = Field()
    is_enabled: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_deleted: bool = Field(default=False)


class UserCreate(UserBase):
    pass


class Users(UserBase, table=True):
    # id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # password: str = Field(min_length=5, max_length=40)
    pass
