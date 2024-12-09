from typing import Generator
import os
from core.config import base_settings 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
# import env obj on basic of dev and prod server
if base_settings.ENV == "test":
    from core.config import test_settings as settings
else:
    from core.config import settings

 

SQLALCHEMY_DATABASE_URL = settings.MYSQL_URL
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
createSessionInstance = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# create a function to create session
def get_sql_db() -> Generator:
    try:
        db = createSessionInstance()
        yield db
    finally:
        db.close()


