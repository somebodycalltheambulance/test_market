from pydantic import BaseModel, EmailStr

#pydantic-схемы для пользователей
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#ну тут всё понятно
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"