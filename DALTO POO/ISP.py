from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        print ("Estoy trabajando")
   
class Comer(ABC):
    @abstractmethod
    def comer(self):
        print ("Estoy comiendo")
        
class Dormir(ABC):
    @abstractmethod
    def dormir(self):
        print ("Estoy durmiendo")
        
class Humano(Trabajador, Dormir, Comer):
    def trabajar(self):
        print("Soy un humano y estoy trabajando")
        
    def comer(self):
        print("Soy un humano y estoy comiendo")
        
    def dormir(self):
        print("Soy un humano y estoy durmiendo")
        
class Robot(Trabajador):
    def trabajar(self):
        print("Soy un robot y estoy trabajando")
        
robot = Robot()
robot.trabajar()

humano = Humano()
humano.trabajar()
    