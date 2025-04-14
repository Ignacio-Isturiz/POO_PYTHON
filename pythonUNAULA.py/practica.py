import numpy as np
class  estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = [notas]
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}: {self.calcularPromedio(promedio)}"
      
    def calcularPromedio(self):
        return np.mean(self.notas)
    
est= estudiante("Ingacio", "Isturiz", [3,5,1,4,3,4])
promedio = est.calcularPromedio()
print(f"{promedio:.2f}")
    