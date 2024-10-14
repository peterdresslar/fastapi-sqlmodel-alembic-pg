from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return {"users": []}

# new user: must post with a name param and an email param. 
# returns the user object with a postgres-generated user id.
# note that the return type is a User object, not a UserCreate object.
@app.post("/users")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)  # adjust port as needed

