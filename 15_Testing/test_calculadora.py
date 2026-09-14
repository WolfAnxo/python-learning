from calculadora import sumar, dividir
import pytest

@pytest.mark.parametrize("a,b, resultado", [
    (2, 3,5),
    (-2, -3, -5),
    (10, 0, 10),
])

def test_sumar_generico(a, b, resultado):
    assert sumar(a,b) == resultado

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

@pytest.fixture
def numeros_para_sumar():
    return (4,6)

def test_sumar_con_fisture(numeros_para_sumar):
    a,b = numeros_para_sumar
    assert sumar(a,b) == 10