import practica

class gestionEstudiante:
    def __init__(self):
        self.estudiantes = []
            
    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        
    def mostrarEstudiantes(self): 
        for est in self.estudiantes:
         print(est)
