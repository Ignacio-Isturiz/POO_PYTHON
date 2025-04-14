class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    @property
    def nombre(self): #property da a entender que get_nombre es una propiedad
        return self.__nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    @nombre.deleter
    def nombre(self):
        return self.__nombre
    
ignacio = Persona("Ignacio",20)

nombre = ignacio.nombre
print(nombre)
        
ignacio.nombre = ("Pepe")

nombre = ignacio.nombre
print(nombre)

ignacio.nombre = ("Pepe")

nombre = ignacio.nombre

del ignacio.nombre

print(nombre)