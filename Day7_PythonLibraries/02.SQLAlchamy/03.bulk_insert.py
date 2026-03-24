from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Fix 1: no space
engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # ✅ Fix 2

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    __table_args__ = (UniqueConstraint('email'),)  # ✅ Fix 3

# Create table
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# ✅ Fix 4: correct emails
users = [
    User(name="Carol", email="carol@example.com"),
    User(name="Dave", email="dave@example.com"),
    User(name="Eve", email="eve@example.com")
]

# ✅ Fix 5: correct method
session.add_all(users)

session.commit()

print("Users inserted successfully")