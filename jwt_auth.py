import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer() 

# 🔑 Clave secreta (usada para firmar el token)
SECRET_KEY = "supersecreto"
ALGORITHM = "HS256"

def create_jwt(data: dict, expires_in: int = 3600):
    """
    data: Diccionario con datos que irán en el token (ej. usuario, rol)
    expires_in: Tiempo en segundos antes de que el token expire (default: 60 seg)
    """
    payload = data.copy()
    payload["exp"] = (datetime.now() + timedelta(seconds=expires_in)).timestamp()

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)  # Crea el JWT

    return token

#verificación del token jwt
def verify_jwt(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401,detail="Token invalido")



@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials  # 📌 Extrae el token
    #token_confirmation = verify_jwt(token)



