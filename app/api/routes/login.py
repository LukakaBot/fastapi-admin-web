from fastapi import APIRouter
from faker import Faker
from app.model.common import ResponseData
from app.model.login import AccountUserTokenParams

router = APIRouter(tags=["login"])

fake = Faker()


@router.post("/user/account/token")
def get_access_token(form_data: AccountUserTokenParams):
    return ResponseData(
        code=200,
        data={
            "userId": fake.random_int(min=100000, max=999999),
            "username": fake.name(),
            "token": fake.uuid4(),
        },
    )


@router.post("/user/info")
def get_user_info(token: str):
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
            "token": token,
            "organizeId": fake.random_int(min=100000, max=999999),
            "organizeName": fake.company(),
        },
    )
