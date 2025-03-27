from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Literal, List

T = TypeVar("T")


class ResponseData(Generic[T], BaseModel):
    code: int = 200
    data: Optional[T] = None
    message: str = "ok"
    type: Literal["success", "error"] = "success"


class ResponsePageData(Generic[T], BaseModel):
    page: int
    pageSize: int
    total: int
    content: list[T] = []


class ResponsePage(Generic[T], BaseModel):
    code: int
    data: ResponsePageData[T]
    message: str = "ok"
    type: Literal["success", "error"] = "success"
