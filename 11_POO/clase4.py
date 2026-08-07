class Persona:
    def __init__(self, nombre, edad, sexo):
            self.nombre = nombre
            self.edad = edad
class Empleado(Persona):
      def __init__(self,nombre, edad, salario):
                  super().__init__(nombre, edad)
                  self.salario = salario