from sqlalchemy import Column, Date, ForeignKey, Integer, String
from .database import Base
from datetime import date

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    reg_date = Column(Date, default=date.today)


class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    publication_date = Column(Date, default=date.today)


class PublicationsTags(Base):
    __tablename__ = "publications_tags"
    
    publication_id = Column(Integer, ForeignKey("publications.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))


class Tags(Base):
    __tablename__ = "tags"
    
    tag_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)