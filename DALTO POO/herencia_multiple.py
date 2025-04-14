class Personas:
    def __init__(self, nombre, edad, nacionalidad):
      self.nombre = nombre
      self.edad = edad
      self.nacionalidad = nacionalidad

    def saludar(self):
        print("Hola, estoy saludando...")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        print(f"Mi habilidad es {self.habilidad}")
        
