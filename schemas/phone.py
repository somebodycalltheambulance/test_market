from pydantic import BaseModel
from enum import Enum

class CategoryEnum(str, Enum):
    ios = "iOS"
    android = "Android"

class PhoneCreate(BaseModel):
    name: str
    description: str
    category: CategoryEnum

class PhoneOut(PhoneCreate):
    id: int

    class Config:
        from_attributes = True
