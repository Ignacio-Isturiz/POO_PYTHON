class Empleado:
    """Clase que representa a un empleado."""

    def __init__(self, nombre, edad, cargo, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario_base = salario_base
        self.salario_total = self.calcular_salario()

    def calcular_salario(self):
        """Calcula el salario total del empleado basado en su cargo."""
        bonificaciones = {
            "Gerente": 500,
            "Desarrollador": 300,
            "Diseñador": 200
        }
        return self.salario_base + bonificaciones.get(self.cargo, 0)

    def mostrar_informacion(self):
        """Muestra la información del empleado."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Cargo: {self.cargo}, Salario: {self.salario_total}")

    
# empleados = []
# opcion = 0

# while opcion != 4:
#     print("\n1. Agregar empleado\n2. Mostrar empleados\n3. Calcular salario\n4. Salir")
#     opcion = int(input("Elige una opción: "))

#     if opcion == 1:
#         nombre = input("Nombre del empleado: ") 
#         edad = int(input("Edad: "))
#         cargo = input("Cargo (Gerente, Desarrollador, Diseñador): ")
#         salario_base = float(input("Salario base: "))

#         if cargo == "Gerente":
#             salario_total = salario_base + 500
#         elif cargo == "Desarrollador":
#             salario_total = salario_base + 300
#         elif cargo == "Diseñador":
#             salario_total = salario_base + 200
#         else:
#             salario_total = salario_base
        
#         empleados.append([nombre, edad, cargo, salario_total])
    
#     elif opcion == 2:
#         for e in empleados:
#             print(f"Nombre: {e[0]}, Edad: {e[1]}, Cargo: {e[2]}, Salario: {e[3]}")
    
#     elif opcion == 3:
#         nombre_buscar = input("Ingrese el nombre del empleado: ")
#         encontrado = False
#         for e in empleados:
#             if e[0] == nombre_buscar:
#                 print(f"El salario de {nombre_buscar} es: {e[3]}")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print("Empleado no encontrado")
    
#     elif opcion == 4:
#         print("Saliendo...")
    
#     else:
#         print("Opción no válida")
