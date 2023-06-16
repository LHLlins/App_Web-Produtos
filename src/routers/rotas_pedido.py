from fastapi import APIRouter, status, Depends, HTTPException 
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido


router = APIRouter()

@router.post('pedidos',status_code = status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedidos(pedido: Pedido, session:Session=Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}', response_model=Pedido)
def exibir_pedidos(id: int, session: Session=Depends(get_db)):
    pedido = RepositorioPedido(session).buscar_pedido(id)
    return pedido


@router.get('/pedidos/{usuario_id}', response_model=List[Pedido])
def listar_pedidos(usuario_id:int, session: Session=Depends(get_db)):
    pedidos  = RepositorioPedido(session).listar_pedidos_usuarios(usuario_id)
    return pedidos

@router.get('/pedidos/{usuario_id}/vendas', response_model=List[Pedido])
def listar_vendas(usuario_id:int, session: Session=Depends(get_db)):
    pedidos  = RepositorioPedido(session).listar_minhas_vendas_usuarios(usuario_id)
    return pedidos