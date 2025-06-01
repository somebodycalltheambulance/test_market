from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin, Token
from repositories.user_repo import get_user_by_email, create_user
from core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException

def register_user(user_data: UserCreate, db: Session):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)
    return create_user(db, user_data.email, hashed_pw)

def login_user(user_data: UserLogin, db: Session) -> Token:
    user = get_user_by_email(db, user_data.email)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="NE TO PALTO")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return Token(access_token=access_token)
