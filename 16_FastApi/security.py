from pwdlib import PasswordHash
import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()

def hashear_password(password):
    return password_hash.hash(password)

def verificar_password(password, hash_guardado):
    return password_hash.verify(password, hash_guardado)

def crear_token(username):
    datos = {"sub" : username}
    expiracion = datetime.now(timezone.utc) + timedelta(minutes=30)
    datos["exp"] = expiracion
    token = jwt.encode(datos, JWT_SECRET, algorithm=ALGORITHM)
    return token

def decodificar_token(token):
    try:
        datos = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return datos
    except jwt.InvalidTokenError:
        return None
