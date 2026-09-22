from fastapi import APIRouter, Depends
from schemas import UsuarioCrear, UsuarioRespuesta
from dependencies import obtener_conexion
from services.usuarios_service import crear_usuario as crear_usuario_service, autenticar_usuario as autenticar_usuario_service
from security import crear_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/", response_model=UsuarioRespuesta, status_code=201)
def crear_usuario(usuario: UsuarioCrear, conexion = Depends(obtener_conexion)):
    return crear_usuario_service(usuario,conexion)

@router.post("/login")
def login(usuario = Depends(OAuth2PasswordRequestForm), conexion = Depends(obtener_conexion) ):
    login_usuario = autenticar_usuario_service(usuario,conexion)
    token =crear_token(login_usuario["username"])
    return {"access_token": token, "token_type": "bearer"}