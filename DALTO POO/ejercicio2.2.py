class Animal:
    def comer(self):
        print("El animal come")
    
class Ave(Animal):
    def volar(self):
        print("El ave vola")

class Mamifero(Animal):
    def amamantar(self):
        print("El mamifero amamanta")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.amamantar()

murcielago.comer()

murcielago.volar()
