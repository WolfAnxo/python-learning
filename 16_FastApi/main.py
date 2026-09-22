from fastapi import FastAPI
from conexion import conectar
from routers.tareas import router as router_tareas
from routers.usuarios import router as router_usuarios

app = FastAPI()
app.include_router(router_tareas)
app.include_router(router_usuarios)

@app.get("/")
def inicio():
    return {"mensaje": "Hola API"}
