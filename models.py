from datetime import date
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    """ Проверяет запрос """
    password: str

class UserResponse(UserBase):
    """ Формирует ответ """
    id: int
    
    class Config:
        orm_mode = True



class PublicationBase(BaseModel):
    title: str
    description:str

class PublicationResponse(PublicationBase):
    """ Формирует ответ """
    publication_date: date
    
    class Config:
        orm_mode = True

class PublicationCreate(PublicationBase):
    """ Проверяет запрос """
    id: int
    owner_id: int



class TagsCreate(BaseModel):
    """ Проверяет запрос """
    name: str

class TagsResponse(BaseModel):
    """ Формирует ответ """
    id: int
    name: str
    
    class Config:
        orm_mode = True
