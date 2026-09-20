from fastapi import FastAPI, HTTPException
from conexion import conectar
from schemas import TareaActualizar, TareaRespuesta, TareaCrear
from routers.tareas import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "Hola API"}
