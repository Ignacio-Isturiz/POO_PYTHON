class encapsulamiento:
    def __init__(self):
        self.__privado = "Esto es un dato privado"
        
    def __metodoPrivado(self):
        print("Este es un método privado")
        

objeto = encapsulamiento()
print(objeto.__metodoPrivado) 

