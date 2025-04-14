# class nombreClase():
#     atributo1 = "valor1"
#     atributo2 = "valor2"
#     atributp3 = "valor3"
    
# objeto = nombreClase()  #<-- Esto es la instancia de la clase, la instancia se crea, creando el objeto                        
# print(objeto.atributo1)

# class Carro():
#     color = "Rojo"
#     marca = "Kia"
#     modelo = "Picanto"
#     anno = "2020"
    
# carro1 = Carro()
# print(carro1.color)  # Imprime: Rojo

class Carro():
    def __init__(self, color, marca, modelo, anno):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.anno = anno      
    
    def arranca(self):
        print(f'Arrancaste con el carro {self.marca} {self.color}')   #METODO PARA ARRANCAR EL CARRO
    
    def parar(self):
        print(f"Paraste el carro {self.marca} {self.color}")   #METODO PARA PARAR EL CARRO                 

carro1 = Carro("Rojo", "Kia", "Picanto", "2020")

carro1.arranca()
     # Imprime: Arrancaste con el carro Kia Rojo