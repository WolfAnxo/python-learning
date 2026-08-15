import sqlite3
from cliente import Cliente
def crear_tabla():
    conexion = sqlite3.connect("clientes.db")

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
    """)

    conexion.close()
    
def mostrar_clientes():
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor() 
    cursor.execute(
        "SELECT * FROM clientes ")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")
    conexion.close()
    

def buscar_cliente():
        conexion = sqlite3.connect("clientes.db")
        cursor = conexion.cursor()
        id_cliente = int(input("ID del cliente que quiere buscar:  "))
        cursor.execute(
            "SELECT * FROM clientes WHERE id = ? ",
            (id_cliente,)
        )

        clientes = cursor.fetchone()
        
        if clientes is not None:
                print(f" ID: {clientes[0]} - Nombre: {clientes[1]} - Edad: {clientes[2]}")
        else: 
             print("No hay ningun cliente con ese ID")
        conexion.close()

def añadir_cliente():

    conexion = sqlite3.connect("clientes.db")

    cursor = conexion.cursor()

    nombre = input("Nombre: ")

    edad = int(input("Edad: "))

    nuevo_cliente = Cliente(nombre, edad)

    cursor.execute(
         " INSERT INTO clientes (nombre, edad) VALUES (?, ?)",
    (nuevo_cliente.nombre, nuevo_cliente.edad)
    )

    conexion.commit()

    print("Cliente añadido correctamente")

    conexion.close()
    
def eliminar_cliente():

    conexion = sqlite3.connect("clientes.db")

    cursor = conexion.cursor()

    mostrar_clientes()

    cliente_eliminado = int(input("ID del cliente que quieres eliminar"))

    cursor.execute(
    "SELECT * FROM clientes WHERE id = ?",
    (cliente_eliminado,)
    )

    clientes = cursor.fetchone()

    if clientes is not None:
          cursor.execute(
                "DELETE FROM clientes WHERE id = ?",
                (cliente_eliminado,)
          )
          conexion.commit()
          print("Cliente eliminado correctamente")
          cursor.execute("SELECT * FROM clientes")
          
          clientes = cursor.fetchall()
          
          for cliente in clientes:
                  print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")
    else:
        print("No hay ningun cliente con ese ID")
    conexion.close()

def modificar_cliente():
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()
    mostrar_clientes()
    modificarcliente = int(input("ID del cliente a modificar "))
    cursor.execute(
         "SELECT * FROM clientes WHERE id = ?",
         (modificarcliente,)
    )
    clientes = cursor.fetchone()

    if clientes is not None:
         nuevo_nombre = input("Nuevo nombre: ")
         nueva_edad = int(input("Nueva edad: "))
         cliente_modificado = Cliente (nuevo_nombre, nueva_edad)
         cursor.execute(
              "UPDATE clientes SET nombre = ? , edad = ? WHERE id = ?",
              (cliente_modificado.nombre , cliente_modificado.edad, modificarcliente)
         )
         conexion.commit()
         print("Cliente modificado correctamente")
         mostrar_clientes()
    else:
          print("No hay ningun cliente con ese ID")
    conexion.close()