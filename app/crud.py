from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Task

from schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session):
    stmt = select(Task).order_by(Task.id)
    
    return list(db.scalars(stmt).all())
    
def get_task(db: Session, task_id):
    return db.get(Task, task_id)

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.model_dump())
    
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception:
        db.rollback()
        raise Exception
    
    return db_task

def update_task(db: Session, task_id, task_data: TaskUpdate):
    db_task = get_task(db, task_id)
    
    if db_task is None:
        return None
    
    changes = task_data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(db_task, field, value)
        
    try:
        db.commit()
        db.refresh(db_task)
    except Exception:
        db.rollback()
        raise Exception
    
    return db_task

def delete_task(db: Session, task_id):
    db_task = get_task(task_id)

    if db_task is None:
        return False
    
    try:
        db.delete(db_task)
        db.commit()
    except Exception:
        db.rollback()
        raise Exception
    
    return True