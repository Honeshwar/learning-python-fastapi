from database import Base # Base is a class that we created in database.py is used to create table by inheriting attribute from this class 
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    __tablename__ = 'todos'

    id=Column(Integer,primary_key=True,index=True)#index=True is used to create unique index some fast accessing data
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    completed=Column(Boolean,default=False)