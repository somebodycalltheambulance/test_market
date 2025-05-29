from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#хеширование пароля тут
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#верификация пароля тут
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#создаем токен при регистрации
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta()
    to_encode.update({"exp":  expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, alghoritm="HS256")
    return encoded_jwt