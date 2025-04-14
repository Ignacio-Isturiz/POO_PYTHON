from codigoFigura import Circulo, Cuadrado, Rectangulo, Trapecio, mostrarFigura

def main():

    circulo = Circulo('Circulo 1', 'rojo', 5)
    cuadrado = Cuadrado('Cuadrado 1', 'azul', 4)
    rectangulo = Rectangulo('Rectangulo 1', 'verde', 5, 6)
    trapecio = Trapecio('Trapecio 1', 'amarillo', 5, 6, 3)
    
    mostrarFigura(circulo)
    mostrarFigura(cuadrado)
    mostrarFigura(rectangulo)
    mostrarFigura(trapecio)
         
# Ejcutar el programa
if __name__ == '__main__':
    main()