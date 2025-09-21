from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db_connection import get_db
from sqlalchemy import text
from .schemas import User, Mesa
import json
from http import HTTPStatus

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

@app.get('/mesas')
async def listas_mesas(db: Session = Depends(get_db)):
    try:
        query = text('''SELECT * FROM public.mesas''')
        result = db.execute(query).mappings().all()
        return result
    except Exception as e:
        print(f'{e}')


@app.post('/mesa/registrar', status_code = HTTPStatus.CREATED)
async def registrar_mesa(id: int,mesa: Mesa, db: Session = Depends(get_db)):

    """ 
        Aqui será onde será inserido as mesas com suas especificações como
        numero, capacidade e status('disponivel','reservada','inativa')    
        """
    
    try:
        user_admin = db.execute(text("SELECT u.role FROM public.usuarios u WHERE u.id = :id"),{"id":id}).scalar_one_or_none() 
        if user_admin == "administrador":
            try:
                query = text('''
                    INSERT INTO public.mesas (numero, capacidade, status) 
                    VALUES (:numero, :capacidade, :status)
                ''')
                db.execute(query, {'numero': mesa.numero, 'capacidade':mesa.capacidade, 'status': mesa.status})
                db.commit()
                return {"Message":f"Mesa:{mesa.numero} adicionada com Sucesso!"}
            except Exception as e:
                db.rollback()
        
        if user_admin is None:
            return HTTPException(status_code = HTTPStatus.NOT_FOUND, detail="Usuario não encontrado")   
        else:
            return HTTPException(status_code = HTTPStatus.UNAUTHORIZED, detail= "Usuario não autorizado.")

    except Exception as e :
        print(f'{e}')

@app.put('/mesas/atualizar', status_code = HTTPStatus.ACCEPTED)
async def atualizar_mesa(id: int,id_mesa: int, mesa: Mesa, db:Session = Depends(get_db)):
    try:
        user_admin = db.execute(text("SELECT u.role FROM public.usuarios u WHERE u.id = :id"),{"id":id}).scalar_one_or_none() 
        if user_admin == "administrador":   
            try:
                update = text('UPDATE public.mesas m SET numero = :numero, capacidade = :capacidade, status = :status WHERE m.id = :id ')
                db.execute(update,{"numero":mesa.numero, "capacidade":mesa.capacidade, "status":mesa.status, "id":id_mesa} )
                db.commit()

            except Exception as e:
                db.rollback()
                return{f"{e}"}
            
    except Exception as e:
        return{f'{e}'}  


# ! Reservas 

@app.get('/mesas/disponibilidade')
async def listar_mesas_disponiveis(capacidade: int ,db: Session = Depends(get_db)):
    query = text("Select * from public.mesas where status = 'disponivel' and capacidade = :capacidade")
    result = db.execute(query, {'capacidade': capacidade}).mappings()
    for row in result:
        print(row)
    