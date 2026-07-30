clientes = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 40}
]

def mostrar_menu():
    print("===== GESTOR DE CLIENTES =====")
    print("1. Mostrar clientes")
    print("2. Buscar clientes")
    print("3. Añadir cliente")
    print("4. Modificar Cliente")
    print("5. Eliminar cliente")
    print("6. Salir")

def mostrar_clientes(clientes):
    for cliente in clientes:
        print(f'{cliente["nombre"]} - {cliente["edad"]} años')

def buscar_cliente(clientes):
    encontrado = False
    nombre = input("¿Qué cliente buscas? ")
    for cliente in clientes:
        if nombre == cliente["nombre"]:
            encontrado = True
            print("Cliente encontrado")
            print(f'Nombre: {cliente["nombre"]}')
            print(f'Edad: {cliente["edad"]}')
            break
    if not encontrado:
        print("Cliente no encontrado")

def añadir_cliente(clientes):
    añadircliente = {
    }
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    añadircliente["nombre"] = nombre
    añadircliente["edad"] = edad
    clientes.append(añadircliente)
    print("Cliente añadido correctamente")

def eliminar_cliente(clientes):
    encontrado = False
    cliente_eliminado = input("Que cliente quieres eliminar: ")
    for cliente in clientes:
        if cliente["nombre"] == cliente_eliminado:
            encontrado = True
            clientes.remove(cliente)
            print ("Cliente eliminado correctamente")
            break
    if not encontrado:
        print("Cliente no encontrado")

def modificar_cliente(clientes):
    encontrado = False
    modificarcliente = input("Que cliente quieres modificar? ")
    for cliente in clientes:
        if cliente["nombre"] == modificarcliente:
            encontrado = True
            nuevonombre = input("Dime el nuevo nombre: ")
            nuevaedad = int(input("Dime la nueva edad: "))
            cliente["nombre"] = nuevonombre
            cliente["edad"] = nuevaedad
            print("Cliente modificado correctamente")
            break
    if not encontrado:
        print("Cliente no encontrado")

while True:
    mostrar_menu()
    opcion = int(input("Que opción eliges? "))

    if opcion == 1:
       mostrar_clientes(clientes)
    elif opcion == 2:
        buscar_cliente(clientes)
    elif opcion == 3:
        añadir_cliente(clientes)
    elif opcion ==4:
        modificar_cliente(clientes)
    elif opcion == 5:
        eliminar_cliente(clientes)
    elif opcion == 6:
        print("Hasta luego")
        break
    else:
     print("Opcion Incorrecta")





