from typing import Any
from pydantic import BaseModel, Field


class UserInSchema(BaseModel):
    login: str
    password: str
    nickname: str

class UserOutSchema(BaseModel):
    id: Any = Field(..., alias='_id')
    login: str
    nickname: str


class UsersOutSchema(BaseModel):
    users: list[UserOutSchema]


class UserModifySchema(BaseModel):
    login: str | None
    nickname: str | None
    password: str | None