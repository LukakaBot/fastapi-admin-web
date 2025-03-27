from fastapi import APIRouter, Header
from typing import Annotated
from faker import Faker
from app.model.common import (
    BaseResponse,
    PageData,
    ResponseSuccess,
)

router = APIRouter(prefix="/user", tags=["user"])

fake = Faker()


# 获取用户信息
@router.get("/info")
def get_user_info(Authorization: Annotated[str | None, Header()] = None):
    if not Authorization:
        return BaseResponse(
            code=401,
            data=None,
            message="Unauthorized",
            type="error",
        )

    return ResponseSuccess(
        data={
            "userId": fake.random_int(min=100000, max=999999),
            "userName": fake.name(),
            "avatar": fake.image_url(),
            "phone": fake.phone_number(),
            "roles": ["admin"],
            "roleName": "admin",
            "menus": [],
            "token": fake.uuid4(),
            "organizeId": fake.random_int(min=100000, max=999999),
            "organizeName": fake.company(),
        },
    )


# 获取用户分页列表
@router.get("/page")
def get_user_page(Authorization: Annotated[str | None, Header()], page: int, size: int):
    if not Authorization:
        return BaseResponse(
            code=401,
            data=None,
            message="Unauthorized",
            type="error",
        )

    users = []

    for _ in range(50):
        users.append(
            {
                "userId": fake.random_int(min=100000, max=999999),
                "userName": fake.name(),
                "avatar": fake.image_url(),
                "phone": fake.phone_number(),
                "roles": ["admin"],
            }
        )

    return BaseResponse(
        code=200,
        data=PageData(
            page=page,
            size=size,
            total=len(users),
            content=users,
        ),
        message="success",
        type="success",
    )
