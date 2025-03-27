from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Literal, List

T = TypeVar("T")


class ResponseData(BaseModel, Generic[T]):
    code: int = 200
    data: Optional[T] = None
    message: str = "ok"
    type: Literal["success", "error"] = "success"


class ResponsePageData(BaseModel, Generic[T]):
    page: int
    pageSize: int
    total: int
    content: list[T] = []


class ResponsePage(BaseModel, Generic[T]):
    code: int
    data: ResponsePageData[T]
    message: str = "ok"
    type: Literal["success", "error"] = "success"
