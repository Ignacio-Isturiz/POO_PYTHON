from gestionEst import gestionEstudiante
from practica import estudiante    
def __main__():
    gestion = gestionEstudiante()
    estudiante1 = estudiante("Juan", "Andes", [4,6,5,2,8])
    estudiante2 = estudiante("Maria", "Torres", [1,3,5,4,6])
    gestion.agregarEstudiante(estudiante1)
    gestion.agregarEstudiante(estudiante2)
    gestion.mostrarEstudiantes()
            
if __name__ == "__main__":
        __main__()

