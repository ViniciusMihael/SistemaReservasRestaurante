from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from decouple import config


engine = create_engine(config('DB_URL_RESTAURANTE'),echo=True,future=True)

Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()