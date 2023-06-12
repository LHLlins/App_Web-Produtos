from fastapi import APIRouter, status, Depends 
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import  Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

router = APIRouter()

# USUARIO
@router.post('/usuarios', status_code = status.HTTP_201_CREATED, response_model =Usuario)
def criar_usuarios(usuario:Usuario, db:Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado 

@router.get('/usuarios',status_code = status.HTTP_200_OK, response_model = List[Usuario])
def listar_usuaio(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.delete('/usuarios/{id}', response_model = Usuario)
def remover_usuaio(id:int, db:Session = Depends(get_db)):
    RepositorioUsuario(db).remover(id)
    return 
