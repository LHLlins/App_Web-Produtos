from fastapi import APIRouter, status, Depends, HTTPException 
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido, Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.routers.auth_utils import obter_usuario_logado


router = APIRouter()

@router.post('pedidos',status_code = status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedidos(pedido: Pedido, session:Session=Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}')
def exibir_pedidos(id: int, session: Session=Depends(get_db)):
    try:
        pedido = RepositorioPedido(session).buscar_pedido(id)
        return pedido
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Não exsiste um pedido com id={id}')

@router.get('/pedidos/{usuario_id}/compras/')
def listar_pedidos(usuario_id:Usuario=Depends(obter_usuario_logado), session: Session=Depends(get_db)):
    pedidos  = RepositorioPedido(session).listar_pedidos_usuarios(usuario_id)
    return pedidos

@router.get('/pedidos/{usuario_id}/vendas')
def listar_vendas(usuario_id:int, session: Session=Depends(get_db)):
    pedidos  = RepositorioPedido(session).listar_minhas_vendas_usuarios(usuario_id)
    return pedidos