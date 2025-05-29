from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    password: str

class UserOut(BaseModel):
    id: int
    is_active: bool
    is_seller: bool

    class Config:
        from_attributes = True
        