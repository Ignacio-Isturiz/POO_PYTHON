#SRP SINGLE RESPONSIBILITY PRINCIPLE

class tanqueCombustible:
    def __init__(self):
        self.combustible = 100
        
    def tanquear(self, cantidad):
        self.combustible += cantidad
        
    def obtener(self):
        return self.combustible
    
    def gasolinear(self, cantidad):
        self.combustible -= cantidad
        
class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def arrancar(self, distancia):
        if self.tanque.obtener() >= distancia / 2:
            self.posicion += distancia
            self.tanque.gasolinear(distancia / 2)
            print("Lo moviste") 
        else:
            print("No hay combustible suficiente")
    
    def obtenerKm(self):
        return self.posicion
        
tanque = tanqueCombustible()
auto = Auto(tanque)

print(auto.obtenerKm())
auto.arrancar(10)
print(auto.obtenerKm())
auto.arrancar(20)
print(auto.obtenerKm())
auto.arrancar(30)
print(auto.obtenerKm())
auto.arrancar(200)
print(auto.obtenerKm())

