from jose import jwt
from datetime import datetime, timedelta


# CONFIG

SECRET_KEY = 'caa9c8nkaslkdjlkajdjdjljajdsabbbalsk'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN =3000

def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + datetime.timedelta(minutes =EXPIRES_IN_MIN)
    dados.update({'exp':expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm = ALGORITHM)

    return token_jwt 


def verificar_acess_token(token: str):
    payload = jwt.decode(token,SECRET_KEY, algorithms = [ALGORITHM])
    return  payload.get('sub')  

