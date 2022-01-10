from fastapi import FastAPI
from .routers import plan, goal, user
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) # Runs the sqlalchemy models and create the database schema

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plan.router)
app.include_router(goal.router)
app.include_router(user.router)


@app.get("/", tags=["Testing"])
def root():
    return {"message":"Hello world"}