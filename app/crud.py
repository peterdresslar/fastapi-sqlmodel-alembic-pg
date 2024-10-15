from sqlmodel import Session, select
from . import models

def get_user_by_email(session: Session, email: str):
    statement = select(models.User).where(models.User.email == email)
    return session.exec(statement).first()

def get_users(session: Session, skip: int = 0, limit: int = 10):
    statement = select(models.User).offset(skip).limit(limit)
    return session.exec(statement).all()

def create_user(session: Session, user: models.User):
    session.add(user)
    session.commit()
    session.refresh(user) # required; otherwise User is stale
    return user

def get_items(session: Session, skip: int = 0, limit: int = 10):
    statement = select(models.Item).offset(skip).limit(limit)
    return session.exec(statement).all()
