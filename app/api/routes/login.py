from fastapi import APIRouter
from faker import Faker
from app.model.common import ResponseError, ResponseSuccess
from app.model.login import AccountUserTokenParams

router = APIRouter(prefix="/login", tags=["login"])

fake = Faker()


@router.post("/account/access-token")
def get_account_access_token(form_data: AccountUserTokenParams):
    if form_data.username != "admin" or form_data.password != "123456":
        return ResponseError(
            message="用户名或密码错误",
        )

    return ResponseSuccess(
        data={
            "userId": fake.random_int(min=100000, max=999999),
            "username": fake.name(),
            "token": fake.uuid4(),
        },
        message="登录成功",
    )
