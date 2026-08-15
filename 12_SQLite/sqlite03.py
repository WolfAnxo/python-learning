import sqlite3

conexion = sqlite3.connect("clientes.db")

cursor = conexion.cursor()

buscar_id = int(input(" ID del cliente: "))

cursor.execute(
    "SELECT * FROM clientes WHERE id = ?",
    (buscar_id,)
)

clientes = cursor.fetchone()


if clientes is not None:
        print(f" ID: {clientes[0]} - Nombre: {clientes[1]} - Edad: {clientes[2]}")
else:
        print("No hay ningun cliente con ese id")

conexion.close()