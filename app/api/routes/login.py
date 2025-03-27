from fastapi import APIRouter
from faker import Faker
from app.model.common import BaseResponse
from app.model.login import AccountUserTokenParams

router = APIRouter(prefix="/login", tags=["login"])

fake = Faker()


@router.post("/account/access-token")
def get_account_access_token(form_data: AccountUserTokenParams):
    if form_data.username != "admin" or form_data.password != "123456":
        return BaseResponse(
            code=401,
            data=None,
            message="用户名或密码错误",
            type="error",
        )

    return BaseResponse(
        code=200,
        message="登录成功",
        type="success",
        data={
            "userId": fake.random_int(min=100000, max=999999),
            "username": fake.name(),
            "token": fake.uuid4(),
        },
    )
