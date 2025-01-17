from sqlmodel import SQLModel, Field, Relationship

# Shared properties
class UserBase(SQLModel):
    name: str
    email: str

# Properties to receive on user creation
class UserCreate(UserBase):
    pass

# Database model, database table name hardcoded to "users"
# adds the autogenerated id that will be returned by postgres
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)

    # table name is actually "users"
    __tablename__: str = "users"

# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)

# Properties to receive on item creation
class ItemCreate(ItemBase):
    owner_id: int

# Database model, database table hardcoded to "items"
class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: int = Field(foreign_key="users.id", nullable=False, ondelete="CASCADE")
    owner: User | None = Relationship(back_populates="items")

    __tablename__: str = "items"

# Read model for items with owner email
class ItemWithOwnerEmail(SQLModel):
    id: int
    title: str
    owner_id: int
    owner_email: str

    class Config:
        from_attributes = True
