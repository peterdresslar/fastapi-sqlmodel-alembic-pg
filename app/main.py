from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return {"users": []}

#new user endpoint. 
# must send a name param and an email param. 
# returns the postgres-generated user id.
@app.post("/users")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user.id

