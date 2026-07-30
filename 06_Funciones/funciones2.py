def sumar(a,b):
    return a + b
resultado = sumar(10, 20)

print(resultado)

def es_mayor_de_edad(edad):
    
    if edad >= 19:
       return True
    else:
        return False
        
años= es_mayor_de_edad(28)
print(años)
años2 = es_mayor_de_edad(10)
print(años2)

clientes = [
    {
        "nombre": "Ana",
        "edad": 25
    },
    {
        "nombre": "Luis",
        "edad": 30
    },
    {
        "nombre": "Pedro",
        "edad": 40
    },
    {
        "nombre": "María",
        "edad": 28
    }
]

def buscar_cliente(clientes, nombre):
    for cliente in clientes:
        if cliente.get("nombre")  == nombre:
            return cliente
    return None

print(buscar_cliente(clientes, "Luis"))
print(buscar_cliente(clientes, "Pedro"))
print(buscar_cliente(clientes, "Carlos"))
