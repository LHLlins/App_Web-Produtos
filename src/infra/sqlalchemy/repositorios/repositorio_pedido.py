from sqlalchemy import update, delete,select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List

class RepositorioPedido():
    
    def __init__(self, session: Session):
        self.session = session

    
    def gravar_pedido(self, pedido:schemas.Pedido):
        pedido_db = models.Pedido(
                                    quantidade=pedido.quantidade,
                                    local_entrega = pedido.local_entrega,
                                    tipo_entrega = pedido.tipo_entrega,
                                    observacoes = pedido.observacoes,
                                    usuario_id = pedido.usuario_id,
                                    produto_id = pedido.produto_id
        )

        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)
        return pedido_db

    def buscar_pedido(self, id:int)->models.Pedido:
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido =  self.session.execute(query).scalar().one()
        return pedido

    def listar_pedidos_usuarios(self, usuario_id:int)->List[models.Pedido]:
        query = select(models.Pedido).where(models.Pedido.usuario_id==usuario_id)
        resultados = self.session.execute(query)
        return resultados
    
    def listar_minhas_vendas_usuarios(self, usuario_id:int)->List[models.Pedido]:
        query = select(models.Pedido)\
            .join_from(models.Pedido,models.Produto)\
            .where(models.Pedido.usuario_id==usuario_id)
        resultados = self.session.execute(query).all()
        return resultados
