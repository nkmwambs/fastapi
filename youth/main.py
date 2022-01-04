from fastapi import FastAPI
from .routers import plan, goal, user

app = FastAPI()

app.include_router(plan.router)
app.include_router(goal.router)
app.include_router(user.router)

@app.get("/",tags=["Testing"])
def root():
    return {"message":"Hello world"}