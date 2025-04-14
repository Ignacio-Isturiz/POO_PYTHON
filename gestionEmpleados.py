from codigoEmpleadoBueno import Empleado

class GestionEmpleados:
    """Clase que gestiona una lista de empleados y sus operaciones."""

    def __init__(self):
        self.empleados = []

    def agregar_empleado(self):
        """Agrega un nuevo empleado a la lista después de solicitar la información al usuario."""
        nombre = input("Nombre del empleado: ")
        edad = self.validar_entrada("Edad: ", int)
        cargo = input("Cargo (Gerente, Desarrollador, Diseñador): ")
        salario_base = self.validar_entrada("Salario base: ", float)

        nuevo_empleado = Empleado(nombre, edad, cargo, salario_base)
        self.empleados.append(nuevo_empleado)
        print(f"✅ Empleado {nombre} agregado con éxito.")

    def mostrar_empleados(self):
        """Muestra la información de todos los empleados registrados."""
        if not self.empleados:
            print("⚠️ No hay empleados registrados.")
        else:
            print("\n📋 Lista de empleados:")
            for empleado in self.empleados:
                empleado.mostrar_informacion()

    def calcular_salario_empleado(self):
        """Calcula y muestra el salario total de un empleado específico buscado por nombre."""
        nombre_buscar = input("Ingrese el nombre del empleado: ")
        empleado = next((e for e in self.empleados if e.nombre.lower() == nombre_buscar.lower()), None)
        
        if empleado:
            print(f"💵 El salario total de {empleado.nombre} es: {empleado.salario_total}")
        else:
            print("❌ Empleado no encontrado.")

    @staticmethod
    def validar_entrada(mensaje, tipo):
        """Valida que la entrada del usuario sea del tipo esperado."""
        while True:
            try:
                return tipo(input(mensaje))
            except ValueError:
                print(f"⚠️ Entrada no válida. Por favor, ingresa un valor {tipo.__name__}.")
