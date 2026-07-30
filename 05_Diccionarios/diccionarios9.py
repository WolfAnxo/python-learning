persona = {
    "nombre": "Anxo",
    "direccion": {
        "ciudad": "Ribeira",
        "pais": "España"
    }
}
print(persona["direccion"]["ciudad"])

persona["direccion"]["pais"] = "Portugal"
print(persona)