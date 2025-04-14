from abc import ABC, abstractmethod

class verificadorOrtografico:
    @abstractmethod
    def verificarPalabra(self, palabra):
        pass
    
class diccionario(verificadorOrtografico):
    @abstractmethod
    def verificarPalabra(self, palabra):
        #logica de verificar palabra en el diccionario
        pass
    
class correctorOrtografico(verificadorOrtografico):
    def __init__(self, verificador):
        self.verificador = verificador
        
    @abstractmethod
    def verificarPalabra(self, palabra):     #logica para corregir texto