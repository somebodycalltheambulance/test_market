from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from utils.hashing import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.pasword)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()