from menu import mostrar_menu
import clientes
while True:
    mostrar_menu()
    opcion = int(input("Que opción eliges? "))

    if opcion == 1:
       clientes.mostrar_clientes()
    elif opcion == 2:
        clientes.buscar_cliente()
    elif opcion == 3:
        clientes.añadir_cliente()
    elif opcion ==4:
        clientes.modificar_cliente()
    elif opcion == 5:
        clientes.eliminar_cliente()
    elif opcion == 6:
        print("Hasta luego")
        break
    else:
     print("Opcion Incorrecta")