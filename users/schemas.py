from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr
from typing import Annotated


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=3, max_length=20)
    username: Annotated[str, MinLen(3), MaxLen(20)]
    password: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr

    class Config:
        json_schema_extra = {
            "CreateUserRequestModel": {
                "username": "any string",
                "password": "any string",
                "email": "need valid email string"
            }
        }

