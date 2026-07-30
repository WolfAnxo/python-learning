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
    }
]

for cliente in clientes:
    print(cliente["nombre"])

for cliente2 in clientes:
    print(f'{cliente2["nombre"]} tiene {cliente2["edad"]} años')

for cliente3 in clientes:
    if cliente3["edad"] > 30:
        print(f'{cliente3["nombre"]} tiene {cliente3["edad"]} años')
