from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import  Usuario, UsuarioSimples, LoginData, LoginSucesso
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_providers, token_providers
from src.routers.auth_utils import obter_usuario_logado


router = APIRouter()

# USUARIO
@router.post('/signup', status_code = status.HTTP_201_CREATED, response_model =UsuarioSimples)
def criar_usuarios(usuario:Usuario, db:Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(db).obter_por_telefone(usuario.telefone)

    if usuario_localizado:
        raise  HTTPException(status_code  = status.HTTP_400_BAD_REQUEST, detail = 'Já existe o usuário' )

    usuario.senha = hash_providers.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado 


@router.post('/token', response_model=LoginSucesso)
def login(login_data : LoginData, session: Session=Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code =status.HTTP_400_BAD_REQUEST, detail ="Usuário incorreto")


    senha_valida = hash_providers.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code =status.HTTP_400_BAD_REQUEST,
                             detail ="Usuário com senha incorreta")

    # GERAR TOKEN
    token = token_providers.criar_acess_token({'sub':usuario.telefone})

    return LoginSucesso(usuario = usuario, acess_topken = token)


@router.get('/me', response_model=UsuarioSimples)
def me(usuario:Usuario = Depends(obter_usuario_logado)):
    return usuario
    

@router.get('/usuarios',status_code = status.HTTP_200_OK, response_model = List[Usuario])
def listar_usuaio(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.delete('/usuarios/{id}', response_model = Usuario)
def remover_usuario(id:int, db:Session = Depends(get_db)):
    RepositorioUsuario(db).remover(id)
    return 
