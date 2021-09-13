from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Authors(str, Enum):
    EDWIN = 'Edwin Garcia'


class BaseThought(BaseModel):
    title: str
    message: str
    author: Authors = Authors.EDWIN

class RequestThought(BaseThought):
    pass

class ResponseThought(BaseThought):
    thought_id: int
    last_updated: datetime
