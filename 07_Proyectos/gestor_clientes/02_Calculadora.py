def mostrar_menu():
    print("===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def sumar():
    while True:
        try:
            numero = int(input(" Dame el primer numero: "))
            numero2 = int(input(" Dame el segundo numero: "))
        
        except ValueError:
            print(" Introduce un numero valido")
        else:
            resultado = numero + numero2
            print(f"{numero} mas {numero2} da como resultado : {resultado}")
            break
def restar():
    while True:
            try:
                numero = int(input(" Dame el primer numero: "))
                numero2 = int(input(" Dame el segundo numero: "))
            
            except ValueError:
                print(" Introduce un numero valido")
            else:
                resultado = numero - numero2
                print(f"{numero} menos {numero2} da como resultado : {resultado}")
                break
def multiplicar():
    while True:
            try:
                numero = int(input(" Dame el primer numero: "))
                numero2 = int(input(" Dame el segundo numero: "))
            
            except ValueError:
                print(" Introduce un numero valido")
            else:
                resultado = numero * numero2
                print(f"{numero} por {numero2} da como resultado : {resultado}")
                break
def dividir():
     while True:
             try:
                 numero = int(input(" Dame el primer numero: "))
                 numero2 = int(input(" Dame el segundo numero: "))
                 resultado = numero / numero2
             
             except ValueError:
                 print(" Introduce un numero valido")
             except ZeroDivisionError:
                  print("No se puede dividir entre cero")
             else:
                 print(f"{numero} entre {numero2} da como resultado : {resultado}")
                 break
while True:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opcion:"))
    except ValueError:
         print("Introduce el numero de la opción")
    else:
        if opcion == 1:
            sumar()
        elif opcion ==2:
         restar()
        elif opcion == 3:
         multiplicar()
        elif opcion == 4 :
         dividir()
        elif opcion == 5:
         break
        elif opcion ==0 or opcion > 5:
            print("Opción incorrecta")