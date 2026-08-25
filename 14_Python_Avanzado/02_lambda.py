#Ejercicio 1:

# cuadrado = lambda numero : numero ** 2

# print(cuadrado(6))

#Ejercicio 2:
clientes = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 32},
    {"nombre": "Marta", "edad": 20}
]

clientes_ordenados = sorted(clientes, key = lambda cliente: cliente["edad"])

print(clientes_ordenados)