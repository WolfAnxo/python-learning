clientes = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Pedro", "edad": 40}
]

while True:
    encontrado = False
    print("1. Mostrar clientes")
    print("2. Buscar cliente")
    print("3. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
            for cliente in clientes:
                print(f'{cliente["nombre"]} - {cliente["edad"] } años ')

    elif opcion == "2":
            encontrar = input("¿Qué cliente buscas?")
            for cliente2 in clientes:
                    if encontrar == cliente2["nombre"]:
                        encontrado = True
                        print("Cliente encontrado")
                        print(f' Edad: {cliente2["edad"]}')
                        break
            if not encontrado:
                print("Cliente no encontrado")

    elif opcion == "3":
            print("Hasta luego")
            break


    else:
        print("Opción incorrecta")
    
