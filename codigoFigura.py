from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    @abstractmethod
    def calcularArea():
        pass
    @abstractmethod
    def calcularPerimetro():
        pass 
    
class Circulo(Figura):
    def __init__(self, nombre, color, radio):
        super().__init__(nombre, color)
        self.radio = radio
    
    def calcularArea(self):
        return 3.1416 * self.radio ** 2
    
    def calcularPerimetro(self):
       return 3.1416 * self.radio * 2
   
class Cuadrado(Figura):
    def __init__(self, nombre, color, lado):
        super().__init__(nombre, color)
        self.lado = lado
        
    def calcularArea(self):
        return self.lado ** 2
    
    def calcularPerimetro(self):
        return 4 * self.lado
        
class Rectangulo(Figura):
    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color)
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura 
    
    def calcularPerimetro(self):
        return 2 * (self.base * self.altura)
    
class Trapecio(Figura):
    def __init__(self, nombre, color, baseMayor, baseMenor, altura):
        super().__init__(nombre, color)
        self.baseMayor = baseMayor
        self.baseMenor = baseMenor
        self.altura = altura
        
    def calcularArea(self):
        return (self.baseMayor + self.baseMenor) / 2 * self.altura
    
    def calcularPerimetro(self):
        return self.baseMayor + self.baseMenor + 2 * (self.baseMayor - self.baseMenor) * self.altura
    
    
def mostrarFigura(figura:Figura):
    print(f"""La figura:{figura.nombre} de color {figura.color} \n
          tiene un area de: {figura.calcularArea()} \n
          y un perimetro de: {figura.calcularPerimetro()}""")
   
    
    

        
    