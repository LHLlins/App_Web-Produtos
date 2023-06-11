from fastapi import FastAPI, Depends,status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProdut
from typing import Optional, List
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


app = FastAPI()

criar_db()


@app.post('/produtos', status_code = status.HTTP_201_CREATED, response_model = ProdutoSimples)
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProdut(db).criar(produto)
    return produto_criado

@app.get('/produtos',status_code = status.HTTP_200_OK, response_model = List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produto_criado = RepositorioProdut(db).listar( )
    return produto_criado


@app.put('/produtos/{id}', response_model = ProdutoSimples)
def editar_produtos(id:int, produto: Produto, db: Session = Depends(get_db)):
    produto_editado = RepositorioProdut(db).editar(id, produto)
    return produto_editado

@app.delete('/produtos/{id}', response_model = Produto)
def remover(id:int, db: Session = Depends(get_db)):
    RepositorioProdut(db).remover(id)
    return 

# USUARIO
@app.post('/usuarios', status_code = status.HTTP_201_CREATED, response_model =Usuario)
def criar_usuarios(usuario:Usuario, db:Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado 

@app.get('/usuarios',status_code = status.HTTP_200_OK, response_model = List[Usuario])
def listar_usuaio(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@app.delete('/usuarios/{id}', response_model = Usuario)
def remover_usuaio(id:int, db:Session = Depends(get_db)):
    RepositorioUsuario(db).remover(id)
    return 
