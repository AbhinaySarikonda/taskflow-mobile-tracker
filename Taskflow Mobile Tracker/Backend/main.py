from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas, crud, auth
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth.register_user(user, db)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return auth.login_user(user, db)

@app.post("/tasks/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/")
def read_tasks(skip: int = 0, limit: int = 10, tag: str = None, status: str = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit, tag=tag, status=status)
