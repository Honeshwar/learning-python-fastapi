from db.base_class import Base
from sqlalchemy import (Column, Integer, String,Enum,DateTime,Text,Boolean,BigInteger)
from sqlalchemy.sql import func #allows you to call SQL functions directly in a Pythonic way when working with SQLAlchemy ORM or Core. eg func.now() corresponds to the SQL NOW() function.
# func.count() corresponds to the SQL COUNT() function.
# func.count() is used to count the number of rows in a table
import enum

# Define a Python Enum for Gender
class GenderEnum(enum.Enum):# enum is used to fixed what can be the value of an attribute
    # class attribute
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


# create team table

'''
nullable=,default = fields are optional in db if not provided it will take default value or None/Null
usage: optional field created, if that column value badh ma milagi 

name required field, if not provide while creating row in db it will throw error
'''
class UserTeam(Base):
    __tablename__ = "user_team"

    id = Column(BigInteger,primary_key=True,index=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    gender = Column(Enum(GenderEnum))
    # nullable=False: Ensures the gender field must have a value.
    mobile = Column(String(10),nullable=True)
    mobile_otp = Column(Integer,nullable=True)
    mobile_otp_verified_at=Column(DateTime,nullable=True)
    email = Column(String(255),nullable=False,unique=True) # false we do when without this value our work not happen
    email_otp_verified_at = Column(DateTime, nullable=True)
    email_otp = Column(Integer,nullable=True)
    graduation_year = Column(Integer,nullable=True)
    college_name    = Column(Text,nullable=True)
    state = Column(String(200),nullable=True)
    zone = Column(String(200),nullable=True)
    checkbox1 = Column(Boolean,nullable=True,default=False)
    checkbox2 = Column(Boolean,nullable=True,default=False)
    team_lead = Column(Boolean,nullable=True,default=False)
    team_id = Column(BigInteger,nullable=True)
    utm_source = Column(Text,nullable=True)
    utm_campaign = Column(Text,nullable=True)
    utm_medium = Column(Text,nullable=True)
    referral = Column(Text,nullable=True)
    created_at = Column(DateTime,nullable=False, server_default=func.now())
    updated_at  = Column(DateTime,nullable=True,server_default=func.now(), onupdate=func.now())
#server_default=func.now() - Sets the default value for the updated_at column to the current timestamp (NOW() in SQL).
# onupdate=func.now() - Automatically updates the updated_at column with the current timestamp every time the record is updated.