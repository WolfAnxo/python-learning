#Ejercicio 1:

# def despedir():
#     print("Adiós")

# def ejecutar(funcion):
#     funcion()

# ejecutar(despedir)


#Ejercicio 2: 

# def mensaje():
#     def mostrar():
#         print("Hola desde la función interna")
#     mostrar()
# mensaje()

#Ejercicio 3:
# def decorador(funcion):

#     def envoltura():
#         print("Inicio")
#         funcion()
#         print("Fin")
#     return envoltura

# @decorador
# def saludar():
#     print("Hola")

# saludar()


#Ejercicio 4

def decorador(funcion):

    def envoltura(*args, **kwargs):
        print("Inicio")
        funcion(*args, **kwargs)
        print("Fin")

    return envoltura


@decorador
def saludar(nombre):
    print(f"Hola {nombre}")


saludar("Ana")






