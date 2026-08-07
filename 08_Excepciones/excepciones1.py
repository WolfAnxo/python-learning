try:
    numero = int(input("Dame un numero: "))

    doblenumero = numero * 2
    print(f"El doble es : {doblenumero}")
except ValueError:
    print("Entrada no valida")

