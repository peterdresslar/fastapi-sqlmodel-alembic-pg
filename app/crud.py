from sqlmodel import Session, select
from app.models import User, Item, UserCreate, ItemCreate, ItemWithOwnerEmail

def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def get_users(session: Session, skip: int = 0, limit: int = 10):
    statement = select(User).offset(skip).limit(limit)
    return session.exec(statement).all()

def create_user(session: Session, user: UserCreate) -> User:
    session.add(user)
    session.commit()
    session.refresh(user) # required; otherwise User is stale
    return user

def get_items_with_owner_emails(session: Session, skip: int = 0, limit: int = 10) -> list[ItemWithOwnerEmail]:
    statement = select(Item, User.email).join(User, Item.owner_id == User.id).offset(skip).limit(limit)
    results = session.exec(statement).all()

    items_with_emails = []
    for item, owner_email in results:
        item_with_email = ItemWithOwnerEmail(
            id=item.id,
            title=item.title,
            owner_id=item.owner_id,
            owner_email=owner_email
        )
        items_with_emails.append(item_with_email)

    return items_with_emails

def create_item(session: Session, item_in: ItemCreate) -> Item:
    session.add(item_in)
    session.commit()
    session.refresh(item_in)
    return item_in
