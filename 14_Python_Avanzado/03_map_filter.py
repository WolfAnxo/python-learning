#Ejercicio 1:

# precios = [10, 25, 50, 100]

# precios_con_iva = list(map(lambda precio : precio * 1.21, precios))

# print(precios_con_iva)

#Ejercicio 2:

edades = [15, 22, 17, 30, 12, 18, 25]

adultos = list(filter(lambda adulto : adulto >= 18 , edades))

print(adultos)