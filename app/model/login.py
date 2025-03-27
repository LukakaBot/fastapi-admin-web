from pydantic import BaseModel


class AccountUserTokenParams(BaseModel):
    username: str
    password: str


class AccountUserTokenResponse(BaseModel):
    userId: str
    username: str
    token: str


class UserInfo(BaseModel):
    userId: str
    userName: str
    avatar: str
    roles: list[str]
    roleName: str
    menus: list[str]
    token: str
    organizeId: str
    organizeName: str
