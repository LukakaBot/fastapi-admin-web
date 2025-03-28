from fastapi import APIRouter, Header
from typing import Annotated
from faker import Faker
from app.model.common import PageData, ResponseSuccess, ResponseError, ResponseCode
from app.service import UserService
from app.model.users import UserCreate, Users
from app.api.deps import SessionDep

router = APIRouter(prefix="/user", tags=["user"])

fake = Faker()


# 获取用户信息
@router.get("/info")
def get_user_info(Authorization: Annotated[str | None, Header()] = None):
    if not Authorization:
        return ResponseError(
            code=ResponseCode.UNAUTHORIZED,
            message="Unauthorized",
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
def get_user_page(
    page: int, size: int, Authorization: Annotated[str | None, Header()] = None
):
    if not Authorization:
        return ResponseError(
            code=ResponseCode.UNAUTHORIZED,
            message="Unauthorized",
        )

    users = []

    for _ in range(size):
        users.append(
            {
                "userId": fake.random_int(min=100000, max=999999),
                "userName": fake.name(),
                "avatar": fake.image_url(),
                "phone": fake.phone_number(),
                "roles": ["admin"],
            }
        )

    return ResponseSuccess(
        data=PageData(
            page=page,
            size=size,
            total=50,
            content=users,
        ),
    )


@router.post("/create")
def create_user(session: SessionDep, params: UserCreate) -> ResponseSuccess[Users]:
    db_user: Users = UserService.create_user(session=session, user=params)

    return ResponseSuccess(
        data=db_user,
    )
