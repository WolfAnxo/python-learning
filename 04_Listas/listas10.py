productos = [
    "Teclado",
    "Ratón",
    "Monitor",
    "Ratón",
    "Auriculares",
    "Ratón"
]
print(productos.count("Ratón"))
try:
    print(productos.index("Ratón"))
except ValueError:
    print("producto no encontrado")
