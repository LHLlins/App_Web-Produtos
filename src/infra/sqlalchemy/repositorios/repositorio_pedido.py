from sqlalchemy import update, delete,select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List

class RepositorioPedido():
    
    def __init__(self, session: Session):
        self.session = session

    
    def gravar_pedido(self, pedido:schemas.Pedido):
        pass


    def buscar_pedido(self, id:int):
        pass

    def listar_pedidos_usuarios(self, usuario_id:int)->List[models.Pedido]:
        pass

    def listar_minhas_vendas_usuarios(self, usuario_id:int)->List[models.Pedido]:
        pass

