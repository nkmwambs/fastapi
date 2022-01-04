from datetime import date, datetime
from pydantic import BaseModel
from pydantic.networks import EmailStr
from sqlalchemy.sql.functions import user
from typing import Optional

class CreatePlan(BaseModel):
    plan_name: str
    plan_start_date: date
    plan_end_date: date

class UserCreate(BaseModel):
    user_email:str
    user_password: str

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





