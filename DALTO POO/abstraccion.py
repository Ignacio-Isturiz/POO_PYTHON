from abc import ABC, abstractmethod

class Figura(ABC):
        @abstractmethod
        def area(self):
            pass
        
        @abstractmethod
        def perimetro(self):
            pass
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
         return self.lado ** 2
    
    def perimetro(self):
         return 4 * self.lado
     
cuadrado = Cuadrado(3)

print("Área:", cuadrado.area())

print("Perímetro:", cuadrado.perimetro())
     
        