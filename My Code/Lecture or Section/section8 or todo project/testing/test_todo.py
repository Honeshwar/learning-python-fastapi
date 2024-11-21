# create database connection for testing 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main import app
from database import Base
from routers.todos import get_db, get_current_user
from fastapi.testclient import TestClient
from models import Todos
import pytest
from sqlalchemy.sql import text

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:h.t%40t566654@localhost:3306/TodoDB'
#  / = %2F and @=  %40
# create instance of database engine/making connection to db
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#each time we use this session instance to access db, bind engine to session
TestingLocalSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)



def override_get_db():
    db = TestingLocalSession()
    try:
        yield db
    finally:
        db.close
def override_get_current_user():
    return None
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


client = TestClient(app)




@pytest.fixture
def test_todo():
    todo = Todos(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

def test_get_all_todos(test_todo):
    response = client.get('/')
    print(response.json())
    assert response.status_code == 200


