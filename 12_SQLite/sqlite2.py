import sqlite3

conexion = sqlite3.connect("clientes.db")

cursor = conexion.cursor()

nombre_cliente = input("Nombre del cliente: ")

edad_cliente = int(input("Edad del cliente: "))

cursor.execute(
    "INSERT INTO clientes (nombre, edad) VALUES (?, ?)",
    (nombre_cliente, edad_cliente)
)

conexion.commit()

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

for cliente in clientes:
    print(f" ID: {cliente[0]} - Nombre: {cliente[1]} - Edad: {cliente[2]}")

conexion.close()