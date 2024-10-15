from sqlmodel import create_engine, Session
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
