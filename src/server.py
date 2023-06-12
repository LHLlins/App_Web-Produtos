from fastapi import FastAPI, Depends,status
from fastapi.middleware.cors import CORSMiddleware

from src.routers import rotas_produtos
from src.routers import rotas_usuarios

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

# ROUTERS
app.include_router(rotas_produtos.router)
app.include_router(rotas_usuarios.router)

