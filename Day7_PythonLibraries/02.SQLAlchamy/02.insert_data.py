from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///example.db')  # ✅ fixed

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # ✅ fixed

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    __table_args__ = (UniqueConstraint('email'),)  # ✅ fixed

# Create table (safe even if already exists)
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
new_user = User(name="Bob", email="bob@example.com")
session.add(new_user)
session.commit()

print("User inserted successfully")