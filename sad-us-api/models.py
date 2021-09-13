from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Authors(str, Enum):
    EDWIN = 'Edwin Garcia'

class Thought(BaseModel):
    title: str
    message: str
    author: Authors = Authors.EDWIN

class ResponseThought(Thought):
    thought_id: int
    last_updated: datetime
