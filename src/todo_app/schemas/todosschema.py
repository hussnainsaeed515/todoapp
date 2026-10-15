from typing import Optional
from pydantic import BaseModel, ConfigDict


# Todo Create Schema (Input - naya todo banana)
class TodoCreate(BaseModel):
    title: str
    description: str


# Todo Update Schema (Input - todo update karna)
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None


# Todo Response Schema (Output - todo return karna)
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_done: bool

    model_config = ConfigDict(from_attributes=True)
