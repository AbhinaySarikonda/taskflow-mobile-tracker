from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas
import hashlib

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(user: schemas.UserCreate, db: Session):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = hash_password(user.password)
    new_user = models.User(username=user.username, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "User created"}

def login_user(user: schemas.UserLogin, db: Session):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or db_user.password != hash_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"msg": "Login successful", "user_id": db_user.id}
