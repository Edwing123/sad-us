from typing import Optional
from pydantic import BaseModel


class Thought(BaseModel):
    title: str
    message: str
    author: str
