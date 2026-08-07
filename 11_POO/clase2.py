class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")

    def cumplir_años(self):
        self.edad = self.edad + 1

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def cambiar_sexo(self, nuevo_sexo):
        self.sexo = nuevo_sexo

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}  \nEdad: {self.edad} \nSexo: {self.sexo}")

ana = Persona("Ana", 25 , "Mujer")
luis = Persona("Luis", 30, "Hombre")
pedro = Persona("Pedro", 18 , "Hombre")

ana.saludar()
luis.saludar()
pedro.saludar()

print(ana.edad)
ana.cumplir_años()
print(ana.edad)

print(f"Nombre: {ana.nombre}  \nEdad: {ana.edad} \nSexo: {ana.sexo}")

ana.cambiar_nombre("María")
ana.cambiar_edad(26)
ana.cambiar_sexo("No binario")

print(f"Nombre: {ana.nombre}  \nEdad: {ana.edad} \nSexo: {ana.sexo}")

print(ana.es_mayor_de_edad())


