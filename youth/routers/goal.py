from fastapi import APIRouter, Depends
from pydantic.tools import T
from .. import models
from ..database import engine
from sqlalchemy.orm import Session
from ..utils import get_db

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/goals",
    tags=["Goals"]
)


# @router.get("/")
# def create_user(db: Session = Depends(get_db)):
#     return {"status": "Success"}

@router.post("/")
def create_goal():
    return {"data":"Hey"}


@router.get("/")
def get_goals():
    return {"message":"Hello world"}


@router.get("/{id}")
def get_goal_by_id():
    return {"data":"Hey"}


@router.put("/{id}")
def update_goal():
    return {"data":"Hey"}


@router.delete("/{id}")
def delete_goal():
    return {"data":"Hey"}