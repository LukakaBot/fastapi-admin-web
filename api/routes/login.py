from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["login"])


class LoginParams(BaseModel):
    username: str
    password: str


@router.post("/login")
def login_access_token(params: LoginParams):
    return {
        "access_token": "Fake access token",
        "token_type": "Bearer",
        **params.model_dump(),
    }
