class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        return NotImplementedError
    
class NotificiacionGmail(Notificacion):
    def notificar(self):
        return f"Notificando por GMAIL {self.usuario},{self.mensaje.gmail}"
    
class NotificiacionInstagram(Notificacion):
    def notificar(self):
        return f"Notificando por IG {self.usuario},{self.mensaje.instagram}"

class NotificiacionWhatsApp(Notificacion):
    def notificar(self):
        return f"Notificando por WS {self.usuario},{self.mensaje.whatsapp}"
    
    