class T9Decoder:
    """Clase que decodifica pulsaciones T9 a texto."""

    def __init__(self):
        # Diccionario con la correspondencia del teclado T9
        self.t9_mapping = {
            '2': "ABC",
            '3': "DEF",
            '4': "GHI",
            '5': "JKL",
            '6': "MNO",
            '7': "PQRS",
            '8': "TUV",
            '9': "WXYZ"
        }

    def decodificar(self, entrada):
        """Decodifica la cadena de entrada T9 a texto."""
        bloques = entrada.split("-")
        resultado = ""

        for bloque in bloques:
            if not self.validar_bloque(bloque):
                return f"❌ Error: El bloque '{bloque}' contiene pulsaciones inválidas."

            tecla = bloque[0]
            repeticiones = len(bloque)

            # Calcula la letra correspondiente según el número de repeticiones
            if tecla in self.t9_mapping:
                letras = self.t9_mapping[tecla]
                indice = (repeticiones - 1) % len(letras)
                resultado += letras[indice]
            else:
                resultado += tecla  # Para caracteres especiales o no mapeados

        return resultado

    @staticmethod
    def validar_bloque(bloque):
        """Valida que el bloque contenga el mismo número repetido."""
        return all(digito == bloque[0] for digito in bloque)


def main():
    """Función principal para ejecutar la decodificación T9."""
    t9_decoder = T9Decoder()
    entrada = input("🔢 Ingresa la secuencia T9 (bloques separados por '-'): ")
    resultado = t9_decoder.decodificar(entrada)
    print(f"📝 Texto decodificado: {resultado}")


if __name__ == "__main__":
    main()
