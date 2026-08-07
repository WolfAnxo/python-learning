try:
    numero = int(input("Dame un numero: "))
except ValueError:
    print("Entrada no valida")
else:
    print("Numero correcto")
finally:
    print("Fin del programa")