persona = {
    "nombre": "Anxo",
    "edad": 25,
    "ciudad": "Ribeira"
}

for dato in persona.keys():
    print(dato)

for dato2 in persona.values():
    print(dato2)

for clave, valor in persona.items():
    print(clave, " -> " , valor)