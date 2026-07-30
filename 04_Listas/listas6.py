clientes = []
while True:
    cliente = input("Introduce un cliente: ")
    if cliente == "salir":
        break
    clientes.append(cliente)

print(f"Clientes registrados: ")
for cliente in clientes:
    print(cliente)