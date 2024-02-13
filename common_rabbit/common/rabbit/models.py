from typing import TypeVar

from pydantic import BaseModel


class RabbitParams(BaseModel):
    responseExchange: str
    responseQueue: str


class BaseRequest(BaseModel):
    id: str


CommonRequest = TypeVar("CommonRequest", bound=BaseRequest)
