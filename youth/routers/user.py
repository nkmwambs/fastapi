from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import schemas, utils, models, auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)

@router.get("/")
def get_users():
    return {"message":"Users"}


@router.get("/{id}")
def get_user_by_id(id: int):
    return {"message":f"Users by id {id}"}


@router.post("/", response_model=schemas.ReturnUser, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):

    check_user = db.query(models.User).filter(models.User.user_email == user.user_email).first()

    if check_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Duplicate email")

    new_user = models.User(
        user_email = user.user_email,
        user_password = auth.hash_password(user.user_password),  
        user_created_by = 0,
        user_created_date = datetime.now(),
        user_last_modified_by = 0)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login")
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(utils.get_db)):

    log_user = db.query(models.User).filter(models.User.user_email == form_data.username).first()

    if not log_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    verify = auth.verify_password(form_data.password, log_user.user_password)

    if not verify:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    token = auth.create_access_token(data={"user_id": log_user.user_id})
    
    return {"access_token": token, "token_type": "bearer"}




