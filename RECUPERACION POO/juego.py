import tkinter as tk
from tkinter import messagebox

class Jugador:
    """Clase que representa a un jugador en el juego"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.numero_secreto = None
        self.intentos = []

    def establecer_numero(self, numero):
        """Establece el número secreto del jugador"""
        if numero.isdigit() and len(numero) == 4:
            self.numero_secreto = numero
            return True
        return False

    def verificar_aciertos(self, intento):
        """Verifica cuántos dígitos están en la posición correcta"""
        return sum(1 for i in range(4) if intento[i] == self.numero_secreto[i])


class JuegoAdivinanza(tk.Tk):
    """Clase principal del juego con Tkinter"""
    def __init__(self):
        super().__init__()

        self.title("Adivina el Número - 2 Jugadores")
        self.geometry("500x450")
        self.resizable(False, False)

        self.jugador1 = Jugador("Jugador 1")
        self.jugador2 = Jugador("Jugador 2")
        self.turno = 1
        self.numero_secreto_establecido = False
        self.jugador1_gano = False

        # Etiqueta principal
        self.label_info = tk.Label(self, text="Jugador 1: Ingresa tu número secreto", font=("Arial", 12))
        self.label_info.pack(pady=10)

        # Campo de entrada
        self.entry_numero = tk.Entry(self, font=("Arial", 14), justify="center", show="*")
        self.entry_numero.pack(pady=5)

        # Botón de enviar
        self.boton_enviar = tk.Button(self, text="Aceptar", font=("Arial", 12), command=self.procesar_entrada)
        self.boton_enviar.pack(pady=10)

        # Etiqueta de resultados
        self.label_resultado = tk.Label(self, text="", font=("Arial", 12))
        self.label_resultado.pack(pady=10)

        # Área de historial
        self.label_historial = tk.Label(self, text="Historial de Intentos", font=("Arial", 12, "bold"))
        self.label_historial.pack(pady=5)

        self.text_historial = tk.Text(self, height=10, width=60, font=("Arial", 10))
        self.text_historial.pack(pady=5)
        self.text_historial.config(state=tk.DISABLED)  # Bloquear edición del historial

    def procesar_entrada(self):
        """Gestiona la lógica del juego según el turno"""
        numero_ingresado = self.entry_numero.get()

        # Fase de elección de números secretos
        if not self.numero_secreto_establecido:
            if self.turno == 1:
                if self.jugador1.establecer_numero(numero_ingresado):
                    self.label_info.config(text="Jugador 2: Ingresa tu número secreto")
                    self.entry_numero.delete(0, tk.END)
                    self.turno = 2
                else:
                    self.label_resultado.config(text="Número inválido. Debe ser de 4 dígitos.", fg="red")
            elif self.turno == 2:
                if self.jugador2.establecer_numero(numero_ingresado):
                    self.label_info.config(text="Jugador 1: Intenta adivinar el número de Jugador 2")
                    self.entry_numero.delete(0, tk.END)
                    self.numero_secreto_establecido = True
                    self.turno = 1
                else:
                    self.label_resultado.config(text="Número inválido. Debe ser de 4 dígitos.", fg="red")
        
        # Fase de adivinanza (turnos alternados)
        else:
            if numero_ingresado.isdigit() and len(numero_ingresado) == 4:
                if self.turno == 1:
                    aciertos = self.jugador1.verificar_aciertos(numero_ingresado)
                    self.jugador1.intentos.append(f"Jugador 1: {numero_ingresado} - {aciertos} aciertos")
                    self.actualizar_historial()
                    
                    self.label_resultado.config(text=f"{self.jugador1.nombre}: {aciertos} dígitos correctos.")
                    
                    if aciertos == 4:  # Jugador 1 acertó el número del Jugador 2
                        self.jugador1_gano = True
                        messagebox.showinfo("¡Acierto!", f"{self.jugador1.nombre} adivinó el número de {self.jugador2.nombre}.\n{self.jugador2.nombre} tiene un intento para empatar.")
                        self.label_info.config(text="Jugador 2: Último intento para empatar")
                        self.turno = 2
                    else:
                        self.label_info.config(text="Jugador 2: Intenta adivinar el número de Jugador 1")
                        self.turno = 2
                elif self.turno == 2:
                    aciertos = self.jugador2.verificar_aciertos(numero_ingresado)
                    self.jugador2.intentos.append(f"Jugador 2: {numero_ingresado} - {aciertos} aciertos")
                    self.actualizar_historial()

                    self.label_resultado.config(text=f"{self.jugador2.nombre}: {aciertos} dígitos correctos.")

                    if aciertos == 4:  # Jugador 2 acertó el número del Jugador 1
                        if self.jugador1_gano:
                            messagebox.showinfo("¡Empate!", "Ambos jugadores adivinaron. ¡Es un empate!")
                        else:
                            messagebox.showinfo("¡Victoria!", f"{self.jugador2.nombre} adivinó el número de {self.jugador1.nombre} y gana el juego.")
                        self.reiniciar_juego()
                    else:
                        if self.jugador1_gano:
                            messagebox.showinfo("¡Juego terminado!", f"{self.jugador1.nombre} gana el juego.")
                            self.reiniciar_juego()
                        else:
                            self.label_info.config(text="Jugador 1: Intenta adivinar el número de Jugador 2")
                            self.turno = 1
            else:
                self.label_resultado.config(text="Número inválido. Debe ser de 4 dígitos.", fg="red")
            
            self.entry_numero.delete(0, tk.END)

    def actualizar_historial(self):
        """Actualiza el historial de intentos"""
        self.text_historial.config(state=tk.NORMAL)
        self.text_historial.delete("1.0", tk.END)

        historial_completo = "\n".join(self.jugador1.intentos + self.jugador2.intentos)
        self.text_historial.insert(tk.END, historial_completo)
        self.text_historial.config(state=tk.DISABLED)

    def reiniciar_juego(self):
        """Reinicia el juego"""
        self.jugador1 = Jugador("Jugador 1")
        self.jugador2 = Jugador("Jugador 2")
        self.turno = 1
        self.numero_secreto_establecido = False
        self.jugador1_gano = False
        self.label_info.config(text="Jugador 1: Ingresa tu número secreto")
        self.label_resultado.config(text="")
        self.entry_numero.delete(0, tk.END)

        # Limpiar historial
        self.text_historial.config(state=tk.NORMAL)
        self.text_historial.delete("1.0", tk.END)
        self.text_historial.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = JuegoAdivinanza()
    app.mainloop()