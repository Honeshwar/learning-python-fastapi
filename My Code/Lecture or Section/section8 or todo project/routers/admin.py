from fastapi import APIRouter
from fastapi import  Depends,Path,Query,HTTPException,Body
 
from models import Todos,User
from typing import Annotated
from sqlalchemy.orm import Session
from database import   LocalSession
from starlette import status

from pydantic import BaseModel, Field
from .auth import get_current_user

 
router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


# create db session

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency =Annotated[dict,Depends(get_current_user)]


@router.get('/get_all_todos',status_code=status.HTTP_200_OK)
def get_all_todos(user:user_dependency,db: db_dependency):
    if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
    elif user.get('role') != 'admin':
          raise HTTPException(status_code=404,detail="user is not admin")
    
    todos  = db.query(Todos).filter(Todos.owner_id == user['user_id']).all()


    return todos
