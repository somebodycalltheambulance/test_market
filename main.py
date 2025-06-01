from fastapi import FastAPI
from api import auth, phones
from db.session import Base, engine
from dotenv import load_dotenv
load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
#app.include_router(phones.router, prefix="/phones", tags=["phones"])