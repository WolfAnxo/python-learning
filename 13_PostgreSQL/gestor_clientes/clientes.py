from cliente import Cliente
from conexion import conectar

def mostrar_clientes():
    conexion = conectar()
    cursor = conexion.cursor() 
    cursor.execute(
        "SELECT * FROM clientes ")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]} - Email: {cliente[3]} - Activo: {cliente[4]}")
    conexion.close()

def buscar_cliente():

    conexion= conectar()
    cursor = conexion.cursor() 
    id_cliente = int(input("ID del cliente a buscar: "))
    cursor.execute(
            "SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()
    if cliente is not None:
        print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]} - Email: {cliente[3]} - Activo: {cliente[4]}")
    else: 
        print("No existe ningun cliente con ese ID")
    conexion.close()

def añadir_cliente():
    conexion = conectar()

    cursor = conexion.cursor() 

    nombre_cliente = input(" Nombre del cliente: ")
    edad_cliente = int(input(" Edad del cliente: "))
    email_cliente = input("Email del cliente: ")

    nuevo_cliente = Cliente(nombre_cliente, edad_cliente, email_cliente)

    cursor.execute(
        "INSERT INTO clientes (nombre, edad , email) VALUES (%s,%s,%s)",
        (nuevo_cliente.nombre, nuevo_cliente.edad, nuevo_cliente.email,)
    )
    conexion.commit()
    mostrar_clientes()
    conexion.close()

def modificar_cliente():
    conexion=conectar()
    
    cursor = conexion.cursor() 

    mostrar_clientes()

    id_modificado = int(input("ID del cliente que quieres modificar: "))

    cursor.execute("SELECT * FROM clientes WHERE id = %s ", (id_modificado,))

    cliente_modificado = cursor.fetchone()

    if cliente_modificado is not None:
        nuevo_nombre = input("Nuevo nombre del cliente: ")
        nueva_edad = int(input("Nueva edad del cliente: "))
        nuevo_email = input("Nuevo email del cliente: ")

        clientemod = Cliente(nuevo_nombre, nueva_edad, nuevo_email)
        cursor.execute("UPDATE clientes SET nombre = %s , edad = %s , email = %s WHERE id = %s", (clientemod.nombre, clientemod.edad, clientemod.email, id_modificado,))
        conexion.commit()
        mostrar_clientes()
        
    else:
        print("No hay ningun cliente con ese ID")
    conexion.close()

def eliminar_cliente():

    conexion= conectar()
        
    cursor = conexion.cursor() 
    
    mostrar_clientes()
    id_eliminar = int(input("ID del cliente que quieres eliminar: "))
    
    cursor.execute("SELECT * FROM clientes WHERE id = %s ", (id_eliminar,))
    
    cliente_eliminado = cursor.fetchone()
    
    if cliente_eliminado is not None:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id_eliminar,))
            conexion.commit()
            print("Cliente eliminado correctamente")
            mostrar_clientes()
            
    else:
            print("No hay ningun cliente con ese ID")
    conexion.close()