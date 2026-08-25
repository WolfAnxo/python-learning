#Ejercicio 1:

# def sumar(*args):
#         return sum(args)

# print(sumar(5, 10))
# print(sumar(5, 10, 20))
# print(sumar(1, 2, 3, 4, 5))

#Ejercicio 2:

# def mostrar_usuario(**kwargs):
#         for clave, valor in kwargs.items():
#                 print(f"{clave} : {valor}")

# mostrar_usuario(nombre ="Ana", edad = 25, ciudad= "Madrid")

#Ejercicio 3:

def mostrar_datos(*args, **kwargs):
    for elemento in args:
        print(elemento)
        
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

mostrar_datos(
    "Python",
    "PostgreSQL",
    "Git",
    nombre="Ana",
    edad=25
)