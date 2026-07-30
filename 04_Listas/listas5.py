encontrado = False

clientes = ["Ana", "Luis", "Pedro", "María", "Carlos"]

buscarcliente = input("¿Qué cliente buscas?")

for cliente in clientes:
    if buscarcliente == cliente:
        encontrado = True
        break

if encontrado == True:
        print("Cliente encontrado")
else:
        print("Cliente no encontrado")
