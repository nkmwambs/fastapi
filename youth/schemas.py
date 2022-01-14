from datetime import date, datetime
from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional

class CreatePlan(BaseModel):
    plan_name: str
    plan_start_date: date
    plan_end_date: date

class UserCreate(BaseModel):
    user_email:str
    user_password: str

class UpdateUser(UserCreate):
    user_email: Optional[str] = None

class ReturnUser(BaseModel):
    user_id: int
    user_email:EmailStr

    class Config:
        orm_mode = True

class ReturnPlan(BaseModel):
    plan_name: str
    plan_start_date: date
    plan_end_date: date
    plan_status: int
    user_id: int
    plan_created_date:date
    plan_last_modified_date: datetime
    owner: ReturnUser
    
    class Config:
        orm_mode = True


class UpdatePlan(BaseModel):
    plan_name: str
    plan_start_date: date
    plan_end_date: date


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None


class CreateGoal(BaseModel):
    goal_name: str 
    theme_id: int 
    plan_id: int 
    goal_description: str 
    goal_period: int

class Plan(BaseModel):
    plan_name: str
    plan_start_date: date
    plan_end_date: date
    plan_status: int
    user_id: int
    plan_created_date:date
    plan_last_modified_date: datetime
    
    class Config:
        orm_mode = True

class ReturnGoal(CreateGoal):
    goal_id: int
    goal_created_date: date
    # plan: ReturnPlan

    class Config:
        orm_mode = True

