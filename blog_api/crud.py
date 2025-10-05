from sqlalchemy.orm import Session
from . import models, schemas


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: int, updated_date: schemas.AuthorCreate):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not db_author:
        return None

    for key, value in updated_date.dict().items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)
    return db_author
