try:
    numero = int(input("Dame un numero para dividir: "))
    numero2= int(input("Dame otro numero para dividir: "))
    resultado = numero / numero2
    print(f"El resultado es : {resultado}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")