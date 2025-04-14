from gestionEmpleados import GestionEmpleados

def main():
    """Función principal para ejecutar el programa de gestión de empleados."""
    gestion = GestionEmpleados()
    opcion = 0

    while opcion != 4:
        print("\n🛠️ Menú de opciones:")
        print("1️⃣  Agregar empleado")
        print("2️⃣  Mostrar empleados")
        print("3️⃣  Calcular salario de un empleado")
        print("4️⃣  Salir")
        
        opcion = GestionEmpleados.validar_entrada("Elige una opción: ", int)

        if opcion == 1:
            gestion.agregar_empleado()
        elif opcion == 2:
            gestion.mostrar_empleados()
        elif opcion == 3:
            gestion.calcular_salario_empleado()
        elif opcion == 4:
            print("👋 Saliendo del programa. ¡Hasta luego!")
        else:
            print("⚠️ Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    main()
