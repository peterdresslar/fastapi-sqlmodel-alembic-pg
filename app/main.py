from fastapi import FastAPI, Depends
from sqlmodel import Session
from . import crud
from .models import UserCreate, User, ItemCreate, Item, ItemWithOwnerEmail
from .database import get_session

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", response_model=list[User])
def get_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    users = crud.get_users(session, skip=skip, limit=limit)
    return users

@app.post("/users", response_model=User)
def create_user(user_in: UserCreate, session: Session = Depends(get_session)):
    user = User.model_validate(user_in)
    return crud.create_user(session, user) # since session is refreshed, should return user with id

@app.get("/items", response_model=list[ItemWithOwnerEmail])
def get_items(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    items = crud.get_items_with_owner_emails(session, skip=skip, limit=limit)
    return items

@app.post("/items", response_model=Item)
def create_item(item_in: ItemCreate, session: Session = Depends(get_session)):
    item = Item.model_validate(item_in)
    return crud.create_item(session, item)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)  # adjust port as needed
