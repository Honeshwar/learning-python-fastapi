# Making Python FastAPI
Install python on your system: that give you python, pip, venv ,..
versions: Python 3.12.7, pip     24.2
## Step1 create an environment
```
- create an environment: python -m venv foldername
- run this environment : foldername\Scripts\activate.bat hit enter
- now environment is running, 

```

## Step2 dependencies installation
```
- pip install "uvicorn[standard]"
- pip install Fastapi 
or 
pip install -r requirement.txt // if you have dependencies files

```

## Step3 creating folder structure and main file
```
MVC Folder Structure

- assets config models routers views
- main.py

- now in main.py file add: Create basic Python Fastapi Application

# import FastAPI application from fastapi 
from fastapi import FastAPI

# create an instance of fastapi application
app = FastAPI()

# using that instance create routes and defines its actions
@app.get('/')
def root():
    return {"root":"success"}


- run a command: uvicorn main:app --reload (can add this also to get custom port : --port 3000)
```

## Step4 Setup DB Configuration and models
```
- pip instal sqlalchemy // ORM that help use to sql database without using sql queries(eg. table create , db connection, table create , CRUD operation)

- pip install pymysql // we are using mysql as db, so sqlalchemy use mysql internally so we have to install it when we pass Database_url as mysql url

- create database.py in config folder an users.py in models folder
- in models folder also create index.py or __init__.py to import all models it it and export at once in main files
----------------------------------------------------
config/database.py:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



# engine create hoga that have db connection string
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:h.t%40t566654@localhost:3306/TodoDB'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# session maker create for an engine that we create about so with it help we crate multiple localSession
# return an object that having capability to crate session with db
CreateLocalSessionInstance = sessionmaker(autocommit= False,autoflush=False,bind=engine)


----------------------------------------------------
models/users.py:

from config.database import Base
from sqlalchemy import Column, Integer,String,Boolean,ForeignKey


class Users(Base):
    __tablename__ = 'users'

    id=Column(Integer,primary_key=True, index=True)
    name=Column(String(255))
    email=Column(String(255),unique=True)
    hash_password=Column(String(255))
    is_active=Column(Boolean,default=True)
    role=Column(String(255))
    mobile=Column(String(255), nullable=True)
```


## Step4 Setup routers for scalebality
```
create v1 folder and inside it index.py and user.py
- define prefix in file to set which file belong to which endpoint and also use app.include_router() method to go from one end point to another
```

## Step 5 create routes 

## Step 6 Deployment
```
pip freeze > requirements.txt

```
