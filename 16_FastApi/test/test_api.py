from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_inicio():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json() ["mensaje"]== "Hola API"

def test_tareas_sin_autenticacion():
    respuesta = cliente.get("/tareas")
    assert respuesta.status_code == 401

def test_login_incorrecto():
    respuesta = cliente.post(
    "/usuarios/login",
    data={
        "username": "usuario_que_no_existe",
        "password": "contraseña_incorrecta"
    }
)
    assert respuesta.status_code == 401

def test_login_correcto():
    respuesta = cliente.post(
        "/usuarios/login",
        data={
            "username": "angel",
            "password": "1234"
        }
    )
    assert respuesta.status_code == 200
    assert "access_token" in respuesta.json()
    assert respuesta.json()["token_type"] == "bearer"

def test_tareas_con_autenticacion():
    respuesta = cliente.post(
            "/usuarios/login",
            data={
                "username": "angel",
                "password": "1234"
            }
        )
    token = respuesta.json()["access_token"]
    respuesta_tareas = cliente.get(
    "/tareas/",
    headers={
        "Authorization": f"Bearer {token}"
    }
)
    assert respuesta_tareas.status_code == 200

def test_fixture_usuario(usuario_prueba):
    assert usuario_prueba["username"] == "usuario_test"

def test_usuario_registrado(usuario_registrado):
    respuesta = usuario_registrado["username"]
    assert respuesta == "usuario_test"

def test_token_invalido():
    respuesta = cliente.get("/tareas/",headers={
            "Authorization": "Bearer token_falso"
        })
    assert respuesta.status_code == 401

   
