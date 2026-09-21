from fastapi import HTTPException
from repositories.tareas_repository import obtener_todas, obtener_por_id, crear_tarea as crear_tarea_db, actualizar_tarea as actualizar_tarea_db,eliminar_tarea as eliminar_tarea_db, obtener_por_prioridad

def listar_tareas(prioridad=None):
    if prioridad is not None:
        return obtener_por_prioridad(prioridad)
    else:
        return obtener_todas()

def obtener_tarea(id):
    tarea_buscada = obtener_por_id(id)
    if tarea_buscada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_buscada

def crear_tarea(tarea):
    return crear_tarea_db(tarea)

def actualizar_tarea(id, datos):
    tarea_buscada =obtener_por_id(id)
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

def eliminar_tarea(id):
    tarea_borrada = eliminar_tarea_db(id)
    if tarea_borrada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_borrada

    
    
