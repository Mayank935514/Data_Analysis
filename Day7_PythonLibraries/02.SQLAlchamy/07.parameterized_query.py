from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Fix URL
engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # ✅ correct

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    __table_args__ = (UniqueConstraint('email'),)  # ✅ correct

# Session
Session = sessionmaker(bind=engine)
session = Session()

# ✅ User input
user_name = input("Enter name to search: ")

# ✅ Query
result = session.query(User).filter_by(name=user_name).all()

# ✅ Print results
print("Search result:", [(u.id, u.name, u.email) for u in result])

session.close()