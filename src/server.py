from fastapi import FastAPI, Depends, status, Request, BackgroundTasks 
from fastapi.middleware.cors import CORSMiddleware

from src.routers import rotas_produtos
from src.routers import rotas_auth
from src.routers import rotas_pedido
import asyncio
from src.jobs.write_notification import write_notification



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

@app.post('/send_email/{email}')
def send_email(email:str, background: BackgroundTasks):
    background.add_task(write_notification,email,'Hello everybody!')

    return {'OK':'Mensagem enviada'}


# # MIDDLEWARE 
@app.middleware('http')
async def processar_tempo_requisicao(request, next):
    
    print("Interceptou Chegada ....")

    response = await next(request)

    print("Interceptou a volta ...")

    return response