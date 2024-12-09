from fastapi import APIRouter, Depends, HTTPException
from db.pydantics.users import AddTeamLeaderModel
from db.database import get_sql_db
from sqlalchemy.orm import Session
from db.models.users import UserTeam

router = APIRouter()
# (
#     prefix="/users",#path in api end with /users. so use below routes
#     tags=["users"],
# )

# from fastapi import Depends
# from typing import Annotated

# # db dependency or injection/
# first arg  = return type, second arg = dependency , this type depend upon something, \
# value of routes func depend upon this methods
# db_injection = Annotated[ Session, Depends(get_db)]

'''
here in routes action no one pass db as args, we us default value for db argument that is an dependency

what is dependency?
dependency is a function that returns a value to be used as a parameter in a function.

-------------------------------------------------------------
Depends() method : it will inject the value return by the method that we pass in it , on run time automatically

usage: on runtime inject some value(value return by method that we pass it Depends() method as arg) to function, variable,...
-------------------------------------------------------------
example:
- get_sql_db: A dependency function that provides the current db session.
- Depends(get_sql_db): Indicates that the route(or route function) depends on the get_sql_db function.
- The output of get_sql_db is automatically injected into the add_team_leader route function.
'''
@router.post("/add-team-leader", status_code=201)
# , response_model=dict)
def add_team_leader(AddLeaderReq: AddTeamLeaderModel,  db: Session = Depends(get_sql_db)):

    existing_leader = db.query(UserTeam).filter(UserTeam.email == AddLeaderReq.email).first()
    if existing_leader:
        raise HTTPException(status_code=409, detail="Team leader with this email already exists")
    
    leader= UserTeam(**AddLeaderReq.model_dump())
    db.add(leader)
    db.commit()
    db.refresh(leader)
    

    return {"message": "Team leader added successfully", "leader": leader}