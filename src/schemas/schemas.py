from pydantic import BaseModel
from typing import Optional, List



class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # minhas_vendas: List[Pedido]
    # meus_produtos: List[Produtos]
    # meus_pedidos: List[Pedido]

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    # detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True


class ProdutoSimples(BaseModel):
    id: Optional[str] = None
    nome: str
    preco: float
   

    class Config:
        orm_mode = True



class Pedido(BaseModel):
      id: Optional[str] = None
      quantidade: int
      entrega: bool = True
      enderço: str
      observacoes: Optional[str] = "Sem observacoes"  






