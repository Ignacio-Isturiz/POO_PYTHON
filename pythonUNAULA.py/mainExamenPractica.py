# from examenpractica import empleadoTC, empleadoMT, mostrarSalario

# def main():
#     print("Sistema de cálculo de salarios (bien hecho)")
#     opcion = input("Tipo de empleado (completo/medio): ").lower()

#     if opcion == "completo":
#         nombre = input("Nombre del empleado: ")
#         salarioBase = float(input("Salario base: "))
#         comision = float(input("Bonificación: "))
#         empleado = empleadoTC(nombre, salarioBase, comision)
#         mostrarSalario(empleado)

#     elif opcion == "medio":
#         nombre = input("Nombre del empleado: ")
#         salarioBase = float(input("Salario base: "))
#         horasTrabajadas = float(input("Horas trabajadas: "))
#         empleado = empleadoMT(nombre, salarioBase, horasTrabajadas)
#         mostrarSalario(empleado)
#     else:
#         print("Opción no válida")
       

from examenpractica import vehiculo, carro, moto, camion, mostrarVehiculo

def main():
    print("🚀 Sistema de alquiler de vehículos 🚗🏍️🚚")
    print("Opciones: Carro | Moto | Camion")
    opcion = input("Seleccione el tipo de vehículo: ").lower()
    
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    dias = int(input("Ingrese el número de días de alquiler: "))
    
    if opcion == "carro":
        vehiculo =  carro(marca, modelo, dias)
        mostrarVehiculo(vehiculo)
    elif opcion == "moto":
        vehiculo = moto(marca, modelo, dias)
        mostrarVehiculo(vehiculo)
    elif opcion == "camion":
        carga = int(input("Ingrese la carga en kg del camión: "))
        vehiculo = camion(marca, modelo, dias, carga)
        mostrarVehiculo(vehiculo)

if __name__ == "__main__":
    main()

