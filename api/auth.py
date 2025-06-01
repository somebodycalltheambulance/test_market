from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal
from schemas.user import UserCreate, UserOut
from services.auth_service import register_user

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(user_data, db)
