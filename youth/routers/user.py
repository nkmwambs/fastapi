from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import schemas, utils, models, auth
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.get("/")
def get_users():
    return {"message": "Users"}


@router.get("/{id}")
def get_user_by_id(id: int):
    return {"message": f"Users by id {id}"}


@router.post("/", response_model=schemas.ReturnUser, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):

    check_user = db.query(models.User).filter(
        models.User.user_email == user.user_email).first()

    if check_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Duplicate email")

    new_user = models.User(
        user_email=user.user_email,
        user_password=auth.hash_password(user.user_password),
        user_created_by=0,
        user_created_date=datetime.now(),
        user_last_modified_by=0)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(utils.get_db)):

    log_user = db.query(models.User).filter(
        models.User.user_email == form_data.username).first()

    if not log_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    verify = auth.verify_password(form_data.password, log_user.user_password)

    if not verify:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    token = auth.create_access_token(data={"user_id": log_user.user_id})

    return {"access_token": token, "token_type": "bearer"}


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ReturnUser)
def update_user(id: int, user: schemas.UpdateUser, db: Session = Depends(utils.get_db), current_user: Optional[str] = Depends(auth.get_current_user)):
    user_query = db.query(models.User).filter(
        models.User.user_id == id, models.User.user_deleted_at == None)

    updated_user = user_query.first()

    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User of id {id} not found")

    user.user_password = auth.hash_password(user.user_password)

    if user.user_email != None:
        user_query.update(user.dict())
    else:
        user_query.update({'user_password':  user.user_password})

    db.commit()

    return updated_user
