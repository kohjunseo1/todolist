from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Todolist(Base):
    __tablename__ = "todolist"

    id = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=True)
    content = Column(String(200), nullable=True)
