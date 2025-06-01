from sqlalchemy import Column, Integer, String, Enum
from db.session import Base
import enum

class CategoryEnum(str, enum.Enum):
    ios = "iOS"
    android = "Android"

class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category = Column(Enum(CategoryEnum))
