empresa = {
    "nombre": "OpenAI",
    "empleados": [
        {
            "nombre": "Ana",
            "puesto": "Programadora"
        },
        {
            "nombre": "Luis",
            "puesto": "Analista"
        }
    ]
}
empresa["empleados"].append(
    {
        "nombre" : "Pedro",
        "puesto" : "DevOps"
    } 

)


for empleadomodificado in empresa["empleados"]:
    if empleadomodificado["nombre"] == "Luis":
        empleadomodificado["puesto"] = "Analista Python"
    print(empresa)

for empleado in empresa["empleados"]:
    print(f' {empleado["nombre"]} trabaja como {empleado["puesto"]}')
