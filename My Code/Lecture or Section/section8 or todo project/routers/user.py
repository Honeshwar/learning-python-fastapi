from fastapi import APIRouter
from fastapi import  Depends,Path,Query,HTTPException,Body
 
from models import Todos,User
from typing import Annotated
from sqlalchemy.orm import Session
from database import   LocalSession
from starlette import status

from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext
 
router = APIRouter(
    prefix='/user',
    tags=['user',]
)


# create password context
bycrpt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# create db session

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency =Annotated[dict,Depends(get_current_user)]



class GetUserRequest(BaseModel):
    id: int
    name: str  
    email: str  
    is_active: bool
    role: str


@router.get('/get_user',response_model=GetUserRequest,status_code=status.HTTP_200_OK)
def get_user(user:user_dependency,db: db_dependency):
     print(user)
     if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
    #  elif user.get('role') != 'admin':
    #       raise HTTPException(status_code=404,detail="user is not admin")
     
     user = db.query(User).filter(User.id == user['user_id']).first()

     if user is None:
          raise HTTPException(status_code=404,detail="user not found")
     
     return user


# pydantic req
class ChangePasswordRequest(BaseModel):
    old_password: str=Field(min_length=3)
    new_password: str=Field(min_length=3)
@router.patch('/change-password',status_code=status.HTTP_204_NO_CONTENT)
def change_password(user:user_dependency,db:db_dependency,change_password_req:ChangePasswordRequest):

    if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
     
    user = db.query(User).filter(User.id == user['user_id']).first()

    if not bycrpt_context.verify(change_password_req.old_password,user.hash_password):
          raise HTTPException(status_code=404,detail="user not found or incorrect old  password")
     
    user.hash_password = bycrpt_context.hash(change_password_req.new_password)
    db.commit()

    print(user)

    return user


@router.patch('/update-mobile',status_code=status.HTTP_204_NO_CONTENT)
async def update_mobile(user:user_dependency,db:db_dependency,mobile_no:int=Query(gt=0)):
     
    if user is None:
          raise HTTPException(status_code=404,detail="user not Authenticated")
     
    if not mobile_no.regex("^[6-9][0-9]{9}$"):
          raise HTTPException(status_code=404,detail="mobile number not valid")
    
    
    user = db.query(User).filter(User.id == user['user_id']).first()
    
     
    user.mobile = mobile_no
    db.commit()

    print(user)

    return user