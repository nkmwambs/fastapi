from typing import List, Optional
from fastapi import APIRouter, status, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from ..schemas import CreatePlan, UpdatePlan
from ..utils import get_db
from ..auth import get_current_user
from youth import models
from datetime import datetime
from enum import Enum
from youth import schemas

router = APIRouter(
    prefix="/plans",
    tags=['Plans']
)


class PlanStatus(str, Enum):
    active = 1,
    inactive = 2


@router.post("/", response_model=schemas.ReturnPlan, status_code=status.HTTP_201_CREATED)
def create_plan(plan: CreatePlan, db: Session = Depends(get_db),
                current_user: Optional[str] = Depends(get_current_user)):
    new_plan = models.Plans(
        plan_name=plan.plan_name,
        plan_start_date=plan.plan_start_date,
        plan_end_date=plan.plan_end_date,
        user_id=current_user.user_id,
        plan_status=1,
        plan_created_by=current_user.user_id,
        plan_created_date=datetime.now(),
        plan_last_modified_by=current_user.user_id
    )

    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return new_plan


@router.get("/", response_model=List[schemas.ReturnPlan], status_code=status.HTTP_200_OK)
def get_plans(plan_status: PlanStatus = PlanStatus.active, db: Session = Depends(get_db),
              current_user: Optional[str] = Depends(get_current_user)):
    plans = db.query(models.Plans).filter(models.Plans.plan_status == plan_status.value,
                                          models.Plans.plan_deleted_at == None).all()

    if not plans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Plans for status {plan_status.name} not found")

    return plans


@router.get("/{id}", response_model=schemas.ReturnPlan, status_code=status.HTTP_200_OK)
def get_plan_by_plan_id(id: int, plan_status: PlanStatus = PlanStatus.active, db: Session = Depends(get_db),
                        current_user: Optional[str] = Depends(get_current_user)):
    plan = db.query(models.Plans).filter(models.Plans.plan_id == id, models.Plans.plan_status == plan_status.value,
                                         models.Plans.plan_deleted_at == None).first()

    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Plan for id {id} and status {plan_status.name} not found")

    return plan


@router.get("/user/{id}", response_model=List[schemas.ReturnPlan])
def get_plan_by_user_id(id: int, plan_status: PlanStatus = PlanStatus.active, db: Session = Depends(get_db),
                        current_user: Optional[str] = Depends(get_current_user)):
    plan = db.query(models.Plans).filter(models.Plans.user_id == id,
                                         models.Plans.plan_status == plan_status.value,
                                         models.Plans.plan_deleted_at == None).all()

    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Plan for user_id {id} and status {plan_status.name} not found")

    return plan


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_plan(id: int, plan: UpdatePlan, db: Session = Depends(get_db),
                current_user: Optional[str] = Depends(get_current_user)):
    plan_query = db.query(models.Plans).filter(
        models.Plans.plan_id == id, models.Plans.plan_deleted_at == None)
    updated_plan = plan_query.first()

    if not updated_plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Plan of id {id} not found")

    plan_query.update(plan.dict())
    db.commit()

    return plan


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plan(id: int, db: Session = Depends(get_db), current_user: Optional[str] = Depends(get_current_user)):
    plan_query = db.query(models.Plans).filter(
        models.Plans.plan_id == id, models.Plans.plan_deleted_at == None)
    delete_plan = plan_query.first()

    if not delete_plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Plan of id {id} not found")

    plan_query.update({'plan_deleted_at': datetime.now()})
    db.commit()

    return {"message": "Plan deleted successsful"}
