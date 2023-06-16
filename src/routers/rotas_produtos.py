from fastapi import APIRouter, status, Depends, HTTPException 
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProdut



router = APIRouter()


# PRODUTO
@router.post('/produtos', status_code = status.HTTP_201_CREATED, response_model = ProdutoSimples)
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProdut(db).criar(produto)
    return produto_criado

@router.get('/produtos',status_code = status.HTTP_200_OK, response_model = List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produto_criado = RepositorioProdut(db).listar( )
    return produto_criado


@router.get('/produtos/{id}')
def exibir_produtos(id:int, db:Session = Depends(get_db)):
    produto_localizado = RepositorioProdut(db).busca_id(id)
    if not produto_localizado:
        raise HTTPException(status_code=404, detail = f'Não há  produto {id}  na loja')
    return produto_localizado


@router.put('/produtos/{id}', response_model = ProdutoSimples)
def editar_produtos(id:int, produto: Produto, db: Session = Depends(get_db)):
    produto_editado = RepositorioProdut(db).editar(id, produto)
    return produto_editado

@router.delete('/produtos/{id}', response_model = Produto)
def remover(id:int, db: Session = Depends(get_db)):
    RepositorioProdut(db).remover(id)
    return 
