while True:
    try:
        numero= int(input("Número: "))
    except ValueError:
        print("Debes introducir un número")
    else: 
        print("Número correcto")
        break
    
    