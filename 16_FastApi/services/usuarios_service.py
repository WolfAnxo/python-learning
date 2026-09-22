from fastapi import HTTPException
from security import hashear_password, verificar_password
from repositories.usuarios_repository import (
    crear_usuario as crear_usuario_db,
    obtener_por_username
)
from psycopg.errors import UniqueViolation


def crear_usuario(usuario, conexion):
    try:
        hash_generado = hashear_password(usuario.password)
        return crear_usuario_db(usuario.username, hash_generado, conexion)
    except UniqueViolation:
        conexion.rollback()
        raise HTTPException(status_code=409, detail="El nombre de usuario ya existe")
def autenticar_usuario(datos, conexion):
    usuario = obtener_por_username(datos.username,conexion)
    if usuario is None:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    if verificar_password(datos.password, usuario["password_hash"]) is False:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return usuario