
from Interfaz import carpeta_abstracta

class Mensaje:
    id_clase = 0
    def __init__(self, destinatario, remitente, asunto, cuerpo):
        Mensaje.id_clase +=1
        self.id=Mensaje.id_clase
        self.destinatario=destinatario
        self.remitente=remitente
        self.asunto=asunto
        self.cuerpo=cuerpo
#mensaje por defecto al llamar al objeto
    def __str__ (self):
        return f"De: {self.remitente}, Para: {self.destinatario}, Asunto: {self.asunto}, Id: {self.id}"