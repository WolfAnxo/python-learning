try:
    numero = int(input("Dame un numero: "))
except ValueError:
    print("Entrada no valida")
else:
    print("Numero correcto")
    triplenumero = numero * 3
    print(f"El triple es : {triplenumero}")