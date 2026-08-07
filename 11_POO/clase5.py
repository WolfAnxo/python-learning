class Animal:

    def hablar(self):
        print("Cada animal tiene su sonido")

class Perro(Animal):

    def hablar(self):
        print("Guau")

class Gato(Animal):

    def hablar(self):
        print("Miau")

perro = Perro()
gato = Gato()

perro.hablar()
gato.hablar()