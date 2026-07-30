producto = {
    "nombre": "Teclado",
    "precio": 50
}

print(producto.get("stock", "Sin stock registrado"))

producto.update({
    "nombre": "Teclado",
    "precio": 55,
    "stock": 20
})

print(producto)

stock = producto.pop("stock")

print(f' Stock eliminado: {stock}')