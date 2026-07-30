usuario = input("Usuario: ")

contraseña = input("Introduce tu contraseña: ")

if usuario == "admin" and contraseña == "python123":
    print("Acceso permitido")
else:
    print("Usuario o contraseña incorrectos")