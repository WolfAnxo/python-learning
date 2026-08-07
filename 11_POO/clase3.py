class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío")
        else:
            self._nombre = nuevo_nombre
ana =Persona("Ana", 25)
ana.nombre = "Maria"
print(ana.nombre)