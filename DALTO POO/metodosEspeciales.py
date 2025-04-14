class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"
    
    def __add__(self, otro):
        nuevoValor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevoValor)
    
salome = Persona("Salome", 19)
ignacio = Persona("Ignacio",20)

nuevoValor = ignacio + salome

print(nuevoValor)