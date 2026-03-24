from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Fix 1
engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # ✅ Fix 2

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    __table_args__ = (UniqueConstraint('email'),)  # ✅ Fix 3

# Session
Session = sessionmaker(bind=engine)
session = Session()

# ✅ Fetch all users
users = session.query(User).all()

for user in users:
    print(user.id, user.name, user.email)

session.close()