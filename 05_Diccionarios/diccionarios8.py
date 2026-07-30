clientes = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30, "telefono": "111111111"},
    {"nombre": "Pedro", "edad": 40}
]

for cliente in clientes:
    print(f' {cliente["nombre"]} - Teléfono: {cliente.get("telefono", "No disponible")}')