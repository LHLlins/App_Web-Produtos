from fastapi import FastAPI, Depends,status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProdut
from typing import Optional, List



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