class Personas:
    def __init__(self, nombre, edad, nacionalidad):
      self.nombre = nombre
      self.edad = edad
      self.nacionalidad = nacionalidad
      
class Empleado(Personas):
    def __init__(self, nombre, edad, nacionalidad, profesion, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.profesion = profesion
        self.salario = salario
        
    def saludar(self):
        print(f" Hola soy {self.nombre} y tengo {self.edad}. Soy de {self.nacionalidad}. Mi profesión es {self.profesion} y gano {self.salario} de dólares al mes.00")

ignacio = Empleado("ignacio", 43, "venezuela","programador",20000000)

print(ignacio.saludar())
        