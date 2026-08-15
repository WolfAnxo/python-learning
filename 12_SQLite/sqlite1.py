import sqlite3

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