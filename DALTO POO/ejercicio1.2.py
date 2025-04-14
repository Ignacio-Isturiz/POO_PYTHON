class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"Estudiando...")
        
    def salir(self):
        print("se acabó")
        
nombre = input('Coloque su nombre:')
edad = input('Coloque su edad:')
grado = input('Coloque su grado:')

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS \n\n
      Estudiante: {estudiante.nombre} \n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
      
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
    elif (estudiar.lower() == "salir"):
        estudiante.salir
    break
    