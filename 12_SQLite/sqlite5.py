import sqlite3

conexion = sqlite3.connect("clientes.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

for cliente in clientes:
    print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")

buscar_id = int(input(" ID del cliente a eliminar: "))

cursor.execute(
    "SELECT * FROM clientes WHERE id = ?",
    (buscar_id,)
)

clientes = cursor.fetchone()

if clientes is not None:
    cursor.execute(
    "DELETE FROM clientes  WHERE id = ?",
    (buscar_id,)
    )

    conexion.commit()
    print("Cliente eliminado correctamente")
    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")
else:
    print("No hay ningun cliente con ese id")