from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root():
    return {"message": "Note end point"}

@api.get("/goal")
def root():
    return {"message": "This is a note endpoint"}