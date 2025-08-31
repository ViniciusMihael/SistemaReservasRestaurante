from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db_connection import get_db
from sqlalchemy import text
from .schemas import User, Mesa

app = FastAPI()


# ! Autenticação e registro de usuarios

@app.post('/user/registrar')
async def registrar_usuario(user: User ,db: Session = Depends(get_db)):
    try:
        query = text('''
            INSERT INTO public.usuarios (nome,email,senha,role)
            VALUES(:nome,:email,:senha,:role)
        ''')
        db.execute(query,{'nome': user.nome, 'email':user.email, 'senha': user.senha, 'role': user.role})
        db.commit()
    except Exception as e:
        print(f'{e}')



# ! Registro de mesas

@app.post('/mesa/registrar')
async def registrar_mesa(mesa: Mesa, db: Session = Depends(get_db)):
    try:
        query = text('''
            INSERT INTO public.mesas (numero, capacidade, status) 
            VALUES (:numero, :capacidade, :status)
        ''')
        db.execute(query, {'numero': mesa.numero, 'capacidade':mesa.capacidade, 'status': mesa.status})
        db.commit()
    except Exception as e :
        print(f'{e}')


@app.get('/mesas')
async def listas_mesas(db: Session = Depends(get_db)):
    try:
        query = text('''
            SELECT * FROM public.mesas
        ''')
        result = db.execute(query).mappings()

        for row in result:
            print(row)

    except Exception as e:
        print(f'{e}')


# ! Reservas 

@app.get('/mesas/disponibilidade')
async def listar_mesas_disponiveis(capacidade: int ,db: Session = Depends(get_db)):
    query = text("Select * from public.mesas where status = 'disponivel' and capacidade = :capacidade")
    result = db.execute(query, {'capacidade': capacidade}).mappings()
    for row in result:
        print(row)
    