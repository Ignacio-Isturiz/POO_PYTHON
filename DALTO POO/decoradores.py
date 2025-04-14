def decorador(parametro):
    def puertaCerrada():
        print("La puerta se encuentra cerrada")
        parametro()
    return puertaCerrada

@decorador
def puertaAbriendo():
    print("La puerta se esta abriendo...")
    
puertaAbriendo()