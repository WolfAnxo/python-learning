from menu import mostrar_menu
import clientes
from datos import lista_clientes
while True:
    mostrar_menu()
    opcion = int(input("Que opción eliges? "))

    if opcion == 1:
       clientes.mostrar_clientes(lista_clientes)
    elif opcion == 2:
        clientes.buscar_cliente(lista_clientes)
    elif opcion == 3:
        clientes.añadir_cliente(lista_clientes)
    elif opcion ==4:
        clientes.modificar_cliente(lista_clientes)
    elif opcion == 5:
        clientes.eliminar_cliente(lista_clientes)
    elif opcion == 6:
        print("Hasta luego")
        break
    else:
     print("Opcion Incorrecta")