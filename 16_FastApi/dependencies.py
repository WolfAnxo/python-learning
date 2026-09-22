from conexion import conectar
from fastapi.security import OAuth2PasswordBearer
from security import decodificar_token
from fastapi import Depends, HTTPException
from repositories.usuarios_repository import obtener_por_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def obtener_conexion():
    conexion = conectar()

    try:
        yield conexion
    finally:
        conexion.close()



def obtener_usuario_actual(token = Depends(oauth2_scheme),conexion = Depends(obtener_conexion)):
    datos = decodificar_token(token)
    if datos is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    username = datos.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    usuario = obtener_por_username(username, conexion)
    if usuario is None: 
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return usuario