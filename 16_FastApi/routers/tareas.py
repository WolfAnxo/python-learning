from schemas import TareaRespuesta,TareaCrear,TareaActualizar
from conexion import conectar
from fastapi import APIRouter, HTTPException
from repositories.tareas_repository import obtener_todas, obtener_por_prioridad, obtener_por_id, crear_tarea as crear_tarea_db, actualizar_tarea as actualizar_tarea_db, eliminar_tarea as eliminar_tarea_db

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("/", response_model=list[TareaRespuesta])
def listar_tareas(prioridad: str | None = None):
    if prioridad is not None:
        return obtener_por_prioridad(prioridad)
    else:
        return obtener_todas()

@router.get("/{id}", response_model=TareaRespuesta)
def obtener_tarea(id: int):
    tarea_buscada= obtener_por_id(id)
    if tarea_buscada is not None:
        return tarea_buscada
    
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.post("/",response_model=TareaRespuesta, status_code=201)
def crear_tarea(tarea: TareaCrear):
    return crear_tarea_db(tarea)
@router.patch("/{id}",response_model=TareaRespuesta)
def actualizar_tarea(id: int, datos: TareaActualizar):
    tarea_buscada = obtener_por_id(id)
    if tarea_buscada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if datos.titulo is not None:
        titulo = datos.titulo
    else:
        titulo = tarea_buscada["titulo"]
    if datos.prioridad is not None:
            prioridad = datos.prioridad
    else:
            prioridad = tarea_buscada["prioridad"]
    return actualizar_tarea_db(id, titulo, prioridad)
@router.delete("/{id}") 
def borrar_tarea(id:int):
    tarea_borrada = eliminar_tarea_db(id)
    if tarea_borrada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    else:
        return {"mensaje" : "Tarea eliminada correctamente"}