from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional, Literal
from enum import IntEnum

T = TypeVar("T")


class ResponseCode(IntEnum):
    """响应码"""

    SUCCESS = 200
    ERROR = 500
    NOT_FOUND = 404
    UNAUTHORIZED = 401


class PageData(BaseModel, Generic[T]):
    """分页信息"""

    page: int = Field(..., description="当前页码")
    size: int = Field(..., description="每页条数")
    total: int = Field(..., description="总条数")
    content: list[T] = Field(default_factory=list[T], description="数据列表")


class BaseResponse(BaseModel, Generic[T]):
    """通用响应基类"""

    code: int
    data: Optional[T] | PageData[T] = Field(default=None, description="响应数据")
    message: str
    type: Literal["success", "error"]


class ResponseSuccess(BaseResponse[T], Generic[T]):
    """成功响应"""

    code: int = Field(default=ResponseCode.SUCCESS, description="状态码", frozen=True)
    message: str = Field(default="ok", description="响应消息", frozen=True)
    type: Literal["success", "error"] = Field(
        default="success", description="响应类型", frozen=True
    )


class ResponseError(BaseResponse[T], Generic[T]):
    """错误响应"""

    code: int = Field(default=ResponseCode.ERROR, description="错误状态码", frozen=True)
    message: str = Field(default="error", description="错误消息", frozen=True)
    type: Literal["success", "error"] = Field(
        default="error", description="响应类型", frozen=True
    )
