from schemas import TareaRespuesta,TareaCrear,TareaActualizar
from fastapi import APIRouter
from services.tareas_service import (
     listar_tareas as listar_tareas_service,
    obtener_tarea as obtener_tarea_service,
    crear_tarea as crear_tarea_service,
    actualizar_tarea as actualizar_tarea_service,
    eliminar_tarea as eliminar_tarea_service
)

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("/", response_model=list[TareaRespuesta])
def listar_tareas(prioridad: str | None = None):
    return listar_tareas_service(prioridad)

@router.get("/{id}", response_model=TareaRespuesta)
def obtener_tarea(id: int):
    return obtener_tarea_service(id)


@router.post("/",response_model=TareaRespuesta, status_code=201)
def crear_tarea(tarea: TareaCrear):
    return crear_tarea_service(tarea)
@router.patch("/{id}",response_model=TareaRespuesta)
def actualizar_tarea(id: int, datos: TareaActualizar):
    return actualizar_tarea_service(id,datos)
@router.delete("/{id}") 
def borrar_tarea(id:int):
    eliminar_tarea_service(id)
    return {"mensaje" : "Tarea eliminada correctamente"}