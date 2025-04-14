class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
juanManuel = Estudiante("Juan Manuel",20,5)
print(juanManuel.grado)