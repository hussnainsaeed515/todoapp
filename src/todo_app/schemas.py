from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field


# 1. User Create Schema (Registration input)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


# 2. User Response Schema (Output without sensitive password)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# 3. Token Schema (JWT authentication response)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Optional helper schema for decoded token data
class TokenData(BaseModel):
    email: Optional[str] = None
