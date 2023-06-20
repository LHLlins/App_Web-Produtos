from fastapi import FastAPI, Depends,status
from fastapi.middleware.cors import CORSMiddleware

from src.routers import rotas_produtos
from routers import rotas_auth
from src.routers import rotas_pedido

app = FastAPI()

origins = ["http://localhost:8080", "https://myapp.veltec.com"]

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS PRODUTOS
app.include_router(rotas_produtos.router)


# ROUTERS USUARIOS  DE SUGURANÇA E AUTENTIFICAÇÃO
app.include_router(rotas_auth.router, prefix="/auth")


# ROUTERS PEDIDOS

app.include_router(rotas_pedido.router)
