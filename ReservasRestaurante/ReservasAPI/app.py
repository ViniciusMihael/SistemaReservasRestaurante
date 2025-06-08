from fastapi import FastAPI, Query
from .schemas import Usuario



app = FastAPI()
            

@app.post("/RestauranteGatito/usuarios/registrar")
async def registrar_usuarios(user: Usuario):
    return {
        "user": user
    }


#! Mudar uma parte#