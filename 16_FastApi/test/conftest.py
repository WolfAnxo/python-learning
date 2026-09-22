import pytest
from fastapi.testclient import TestClient
from main import app
from conexion import conectar

cliente = TestClient(app)

@pytest.fixture
def usuario_prueba():
    usuario_prueba = {"username": "usuario_test",
    "password": "test1234"}
    return usuario_prueba

@pytest.fixture
def usuario_registrado(usuario_prueba):
    respuesta = cliente.post("/usuarios/", json = usuario_prueba)
    yield respuesta.json()
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE username  = %s", (usuario_prueba["username"],))
    conexion.commit()
    conexion.close()


    