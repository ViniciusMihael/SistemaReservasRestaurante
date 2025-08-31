from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from decouple import config


engine = create_engine(config('DB_URL_RESTAURANTE'),echo=True,future=True)

Session = sessionmaker(bind=engine)

# with session as conn:
#     try:
#         query = text('SELECT * FROM public.usuarios')
#         result = conn.execute(query).fetchall()
        
#         for row in result:
#             print(row) 

#         conn.commit()
#     except Exception as e:
#         print(f'{e}')

#     finally:
#         conn.close()



def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()