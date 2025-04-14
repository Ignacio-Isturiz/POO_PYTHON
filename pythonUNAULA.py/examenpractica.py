# # Código espagueti: Sin herencia, polimorfismo, abstracción ni SRP

# def calcular_salario_empleado_tiempo_completo(nombre, salario_base, bonificacion):
#     salario_total = salario_base + bonificacion
#     print(f"Empleado: {nombre}")
#     print(f"Salario total (tiempo completo): {salario_total}\n")


# def calcular_salario_empleado_medio_tiempo(nombre, salario_base, horas_trabajadas):
#     salario_por_hora = salario_base / 160  # Asumiendo 160 horas al mes
#     salario_total = salario_por_hora * horas_trabajadas
#     print(f"Empleado: {nombre}")
#     print(f"Salario total (medio tiempo): {salario_total}\n")


# def main():
#     print("Sistema de cálculo de salarios (mal hecho)")

#     opcion = input("Tipo de empleado (completo/medio): ").lower()

#     if opcion == "completo":
#         nombre = input("Nombre del empleado: ")
#         salario_base = float(input("Salario base: "))
#         bonificacion = float(input("Bonificación: "))
#         calcular_salario_empleado_tiempo_completo(nombre, salario_base, bonificacion)

#     elif opcion == "medio":
#         nombre = input("Nombre del empleado: ")
#         salario_base = float(input("Salario base: "))
#         horas_trabajadas = float(input("Horas trabajadas: "))
#         calcular_salario_empleado_medio_tiempo(nombre, salario_base, horas_trabajadas)

#     else:
#         print("Opción no válida")

#codigo resuelto
# main()
# from abc import ABC, abstractmethod
# class empleado(ABC):
#     def __init__(self, nombre, salarioBase):
#         self.nombre = nombre
#         self.salarioBase = salarioBase

#     @abstractmethod
#     def calcularSalario(self):
#         pass
    
# class empleadoTC(empleado):
#     def __init__(self, nombre, salarioBase, comision):
#         super().__init__(nombre, salarioBase)
#         self.comision = comision 
#     def calcularSalario(self):
#             return self.salarioBase + self.comision
        
# class empleadoMT(empleado):
#     def __init__(self, nombre, salarioBase, horasTrabajadas):
#         super().__init__(nombre, salarioBase)
#         self.horasTrabajadas = horasTrabajadas
#     def calcularSalario(self):          
#         salarioPorHora = self.salarioBase / self.horasTrabajadas
#         return salarioPorHora * self.horasTrabajadas
            
        
# def mostrarSalario(empleado: empleado):
#     print(f"Empleado: {empleado.nombre}")
#     print(f"Salario total: {empleado.calcularSalario()}\n")



from abc import ABC, abstractmethod

class vehiculo(ABC):
    def __init__(self, marca, modelo, dias):
        self.marca = marca
        self.modelo = modelo
        self.dias = dias
        
    @abstractmethod
    def calcularCosto(self):
        pass

class carro(vehiculo):
    def calcularCosto(self):
        costoBase = 50 * self.dias
        if self.dias > 7:
            costoBase += (self.dias - 7) * 20  # Costo extra
        return costoBase
    
class moto(vehiculo):
    def calcularCosto(self):
        costoBase = 50 * self.dias
        if self.dias > 7:
            costoBase += (self.dias - 7) * 20 
        return costoBase

class camion(vehiculo):
    def __init__(self, marca, modelo, dias, carga):
        super().__init__(marca, modelo, dias)
        self.carga = carga
        
    def calcularCosto(self):
        costoBase = 80 * self.dias
        if self.carga > 5000:
            costoBase += 50
        return costoBase

def mostrarVehiculo(vehiculo: vehiculo):
    print(f"El vehiculo {vehiculo.marca}({vehiculo.modelo}), tuvo un costo total de: {vehiculo.calcularCosto()}")