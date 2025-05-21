from sqlalchemy.orm import Session
import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10, tag=None, status=None):
    query = db.query(models.Task)
    if tag:
        query = query.filter(models.Task.tag == tag)
    if status:
        query = query.filter(models.Task.status == status)
    return query.offset(skip).limit(limit).all()
