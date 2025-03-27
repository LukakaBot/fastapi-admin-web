from fastapi import APIRouter, Header
from typing import Annotated
from faker import Faker
from app.model.common import ResponseData

router = APIRouter(prefix="/user", tags=["user"])

fake = Faker()


@router.get("/info")
def get_user_info(Authorization: Annotated[str | None, Header()] = None):
    if not Authorization:
        return ResponseData(
            code=401,
            data=None,
            message="Unauthorized",
            type="error",
        )

    return ResponseData(
        code=200,
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
