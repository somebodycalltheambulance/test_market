from pydantic import BaseModel, EmailStr

#то что принимает
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#то что отдает(чтобы не запалить пароль например)
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    