from sqlalchemy import Column, Integer, String
from config.database import Base  # import from config folder

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), index=True)
