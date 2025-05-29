from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


#Создаем сессию БД
engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
