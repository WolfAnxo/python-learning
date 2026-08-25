####BLOQUE 1: LIST COMPREHENSIONS BASICAS####

# Ejercicio 1:

# numeros = [2, 5, 8, 10, 15]

# dobles = [numero * 2 for numero in numeros]

# print(dobles)

#Ejercicio 2:

#numeros = [3, 8, 12, 5, 20, 7, 14]

#mayores = [ numero for numero in numeros if numero >10]

#print(mayores)

#Ejercicio 3:

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#cuadrado_pares = [numero ** 2 for numero in numeros if numero % 2 == 0]

#print(cuadrado_pares)

#Ejercicio 4:

#nombres = ["Ana", "Alejandro", "Luis", "Marta", "Alberto", "Eva"]

#nombres_a = [ nombre.upper() for nombre in nombres if nombre.startswith("A")]

#print(nombres_a)

#Ejercicio 5:

#productos = ["Teclado", "Ratón", "Monitor", "PC", "Auriculares", "USB"]

#productos_largos = [producto.lower() for producto in productos if len(producto) > 5]

#print(productos_largos)

#Ejercicio 6:

#edades = [15, 22, 17, 30, 12, 18]

#clasificacion = [ "Adulto" if edad >= 18 else "Menor" for edad in edades]

#print(clasificacion)

#Ejercicio 7:

#numeros = [5, -3, 8, -1, 0, 12, -7]

#resultado = [0 if numero < 0 else numero for numero in numeros]

#print(resultado)

#Ejercicio 8:

#notas = [3, 5, 7, 9, 4, 6, 10]

#resultados  = [ "Suspenso" if nota < 5 else "Aprobado" if nota < 7 else "Notable" for nota in notas]

#print(resultados)

####BLOQUE 2: LIST COMPREHENSIONS NIVEL MEDIO####

#Ejercicio 9:

#matriz = [
 #   [1, 2, 3],
 #   [4, 5, 6],
 #   [7, 8, 9]
#]

#matriz_ordenada =  [ numero for fila in matriz for numero in fila ]

#print(matriz_ordenada)

#Ejercicio 10: 

#matriz = [
 #   [1, 2, 3],
  #  [4, 5, 6],
  #  [7, 8, 9]
#]

#pares = [ numero for fila in matriz for numero in fila if numero % 2 == 0 ]

#print(pares)

#Ejercicio 11:

#colores = ["rojo", "azul"]
#tallas = ["S", "M", "L"]

#color_talla = [ (color,talla) for color in colores for talla in tallas]

#print(color_talla)

#Ejercicio 12:

#numeros1 = [1, 2, 3]
#numeros2 = [1, 2, 3]

#numeros_combinados = [ (numero1, numero2) for numero1 in numeros1 for numero2 in numeros2 if numero1 != numero2]

#print(numeros_combinados)

#Ejercicio 13:

#clientes = [
  #  {"nombre": "Ana", "edad": 25},
  #  {"nombre": "Luis", "edad": 17},
   # {"nombre": "Marta", "edad": 32},
  #  {"nombre": "Pedro", "edad": 15},
   # {"nombre": "Lucía", "edad": 28}
#]

#clientes_adultos = [cliente["nombre"] for cliente in clientes if cliente["edad"] >= 18]

#print(clientes_adultos)

# Ejercicio 14:

#productos = [
#    {"nombre": "Teclado", "precio": 49.99},
#    {"nombre": "Ratón", "precio": 19.99},
#    {"nombre": "Monitor", "precio": 199.99},
#    {"nombre": "USB", "precio": 9.99},
#    {"nombre": "Auriculares", "precio": 79.99}
#]

#productos_caros = [ producto["nombre"].upper() for producto in productos if producto ["precio"] >= 50]

#print(productos_caros)

# Ejercicio 15:

# alumnos = [
#     {"nombre": "Ana", "notas": [8, 7, 9]},
#     {"nombre": "Luis", "notas": [4, 5, 3]},
#     {"nombre": "Marta", "notas": [10, 9, 8]},
#     {"nombre": "Pedro", "notas": [5, 6, 5]}
# ]

# aprobados = [alumno["nombre"] for alumno in alumnos if sum(alumno["notas"])/ len(alumno["notas"]) >= 5]

# print(aprobados)

####BLOQUE 3: DICTIONARY COMPREHENSIONS####

# Ejercicio 16:

#numeros = [1, 2, 3, 4, 5]

#cuadrados = {numero : numero ** 2 for numero in numeros}

#print(cuadrados)

#Ejercicio 17:

#numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#cuadrados_pares = {numero : numero ** 2 for numero in numeros if numero % 2 ==0}

#print(cuadrados_pares)

#Ejercicio 18:

# precios = {
#     "teclado": 50,
#     "raton": 20,
#     "monitor": 200,
#     "auriculares": 80
# }

# precios_con_iva = {producto : precio + (precio * 21/100) for producto, precio in precios.items()}

# print(precios_con_iva)

#Ejercicio 19:

# productos = {
#     "teclado": 50,
#     "raton": 20,
#     "monitor": 200,
#     "usb": 10,
#     "auriculares": 80
# }

# productos_caros = {producto : precio for producto, precio in productos.items() if precio >= 50}

# print(productos_caros)

#Ejercicio 20:

# usuarios = {
#     "Ana": "ana@email.com",
#     "Luis": "luis@email.com",
#     "Marta": "marta@email.com"
# }

# usuarios_por_email = {email : nombre for nombre, email in usuarios.items()}

# print(usuarios_por_email)

# Ejercicio 21:

# alumnos = [
#     {"nombre": "Ana", "nota": 8},
#     {"nombre": "Luis", "nota": 4},
#     {"nombre": "Marta", "nota": 9},
#     {"nombre": "Pedro", "nota": 5}
# ]

# resultados = {alumno["nombre"] : "Aprobado" if alumno["nota"] >=5 else "Suspenso" for alumno in alumnos }

# print(resultados)

####BLOQUE 4: SET COMPREHENSIONS####

# Ejercicio 22:

# nombres = ["Ana", "Luis", "Ana", "Marta", "Luis", "Pedro", "Marta"]

# nombres_unicos = {nombre.upper() for nombre in nombres}

# print(nombres_unicos)