from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TaskBase(BaseModel):
    title: str
    description: str
    tag: str
    status: str

class TaskCreate(TaskBase):
    owner_id: int

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
