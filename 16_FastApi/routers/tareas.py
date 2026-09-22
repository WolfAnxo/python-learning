from schemas import TareaRespuesta,TareaCrear,TareaActualizar
from fastapi import APIRouter, Depends
from services.tareas_service import (
     listar_tareas as listar_tareas_service,
    obtener_tarea as obtener_tarea_service,
    crear_tarea as crear_tarea_service,
    actualizar_tarea as actualizar_tarea_service,
    eliminar_tarea as eliminar_tarea_service,
)
from dependencies import obtener_conexion, obtener_usuario_actual

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)


@router.get("/", response_model=list[TareaRespuesta])
def listar_tareas(prioridad: str | None = None, conexion = Depends(obtener_conexion),usuario_actual = Depends(obtener_usuario_actual)):
    return listar_tareas_service(prioridad, conexion, usuario_actual["id"])

@router.get("/{id}", response_model=TareaRespuesta)
def obtener_tarea(id: int, conexion = Depends(obtener_conexion),usuario_actual=Depends(obtener_usuario_actual)):
    return obtener_tarea_service(id,conexion, usuario_actual["id"])


@router.post("/",response_model=TareaRespuesta, status_code=201)
def crear_tarea(tarea: TareaCrear, conexion = Depends(obtener_conexion),usuario_actual=Depends(obtener_usuario_actual)):
    return crear_tarea_service(tarea,usuario_actual["id"], conexion)

@router.patch("/{id}",response_model=TareaRespuesta)
def actualizar_tarea(id: int, datos: TareaActualizar, conexion = Depends(obtener_conexion),usuario_actual=Depends(obtener_usuario_actual)):
    return actualizar_tarea_service(id,datos, conexion,usuario_actual["id"])

@router.delete("/{id}") 
def borrar_tarea(id:int, conexion = Depends(obtener_conexion),usuario_actual=Depends(obtener_usuario_actual)):
    eliminar_tarea_service(id, conexion, usuario_actual["id"])
    return {"mensaje" : "Tarea eliminada correctamente"}