
#Ejercicio1

# lenguajes = ["Python", "Java", "JavaScript"]

# lenguaje = iter(lenguajes)

# print(next(lenguaje))
# print(next(lenguaje))
# print(next(lenguaje))
# print(next(lenguaje))

#Ejercicio 2:

class Contador:

    def __init__(self, limite):
        self.actual = 1
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual <= self.limite:
            numero = self.actual
            self.actual += 1
            return numero
        else:
            raise StopIteration

contador = Contador(3)

for numero in contador:
    print(numero)
