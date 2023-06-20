from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select, delete

class RepositorioUsuario():

    def __init__(self, db:Session):
        self.db = db


    def criar(self, usuario: schemas.Usuario):
        usuario_db = models.Usuario(nome = usuario.nome,
                                    senha = usuario.senha,
                                    telefone = usuario.telefone)
        self.db.add(usuario_db)
        self.db.commit()
        self.db.refresh(usuario_db)
        return usuario_db
    
    
    def listar(self):
        stmt = select(models.Usuario)
        usuarios  = self.db.execute(stmt).scalars().all()
        return usuarios

    def remover(self, id : int):
        delete_stmt = delete(models.Usuario).where(models.Usuario.id == id)

        self.db.execute(delete_stmt)
        self.db.commit()
        

    def obter_por_telefone(self, telefone):
        query = select(models.Usuario).where(models.Usuario.telefone == telefone)
        return self.db.execute(query).scalars().first()
      