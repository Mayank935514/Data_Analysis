from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # ✅ double underscore

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    __table_args__ = (UniqueConstraint('email'),)   # ✅ no space + double underscore

Base.metadata.create_all(engine)

print("Table created successfully")