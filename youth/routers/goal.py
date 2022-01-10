from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from youth.auth import get_current_user
from .. import models,schemas
from sqlalchemy.orm import Session
from ..utils import get_db

router = APIRouter(
    prefix="/goals",
    tags=["Goals"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReturnGoal)
def create_goal(goal: schemas.CreateGoal, db: Session = Depends(get_db), current_user: Optional[str] = Depends(get_current_user)):

    history_fields = {"goal_created_by":current_user.user_id,"goal_created_date":datetime.now(), "goal_last_modified_by":current_user.user_id}
    goal_dict = {**goal.dict(),**history_fields}

    new_goal = models.Goals(**goal_dict)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal


@router.get("/plan/{plan_id}", response_model=List[schemas.ReturnGoal])
def get_plan_goals(plan_id: int, db: Session = Depends(get_db)):
    
    goal_query = db.query(models.Goals).filter(models.Goals.plan_id == plan_id, models.Goals.goal_deleted_at == None).all()

    if not goal_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Goals for plan_id {plan_id} not found")
    
    return goal_query


@router.get("/{id}", response_model=List[schemas.ReturnGoal])
def get_goals_by_Id(id: int, db: Session = Depends(get_db)):
    goal_query = db.query(models.Goals).filter(models.Goals.goal_id == id, models.Goals.goal_deleted_at == None).all()
    
    if not goal_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Goals for plan_id {id} not found")

    return goal_query


@router.put("/{id}")
def update_goal():
    return {"data":"Hey"}


@router.delete("/{id}")
def delete_goal():
    return {"data":"Hey"}