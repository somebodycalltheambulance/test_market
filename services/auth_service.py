from sqlalchemy.orm import Session
from schemas.user import UserCreate
from repositories.user_repo import get_user_by_email, create_user
from core.security import hash_password
from fastapi import HTTPException

def register_user(user_data: UserCreate, db: Session):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)
    return create_user(db, user_data.email, hashed_pw)
