import sqlite3

conexion = sqlite3.connect("clientes.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

for cliente in clientes:
    print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")

buscar_id = int(input(" ID del cliente a modificar: "))

cursor.execute(
    "SELECT * FROM clientes WHERE id = ?",
    (buscar_id,)
)

clientes = cursor.fetchone()

if clientes is not None:

    nuevo_nombre = input(" Nuevo nombre: ")
    nueva_edad = int(input(" Nueva edad: ")) 
    cursor.execute(
    "UPDATE clientes SET nombre = ?, edad = ? WHERE id = ?",
    (nuevo_nombre, nueva_edad, buscar_id)
    )

    conexion.commit()
    cursor.execute(
    "SELECT * FROM clientes WHERE id = ?",
    (buscar_id,)
    )

    clientes = cursor.fetchone()
    print(f" ID: {clientes[0]} - Nombre: {clientes[1]} - Edad: {clientes[2]}")
else:
    print("No hay ningun cliente con ese id")

