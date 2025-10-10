
from MainMensaje import Mensaje
from Interfaz import carpeta_abstracta

class Carpeta(carpeta_abstracta):
    def __init__(self, propietario, nombre):
        self.propietario=propietario
        self.nombre=nombre
        self.__mensaje=[
            
        ]
#operaciones internas relacionadas a mensajes
    def get_mensaje(self):
        for mensaje in self.__mensaje:
            return mensaje
    def EnviarMensajes(self, id_mensaje):
        for mensaje in self.__mensaje:
            if mensaje.id == id_mensaje:
                self.propietario.servidor.EnviarMensajes(mensaje)
    def RecibirMensajes(self, mensaje):
        self.__mensaje.append(mensaje)
    def RedactarMensajes(self,destinatario, remitente, asunto, cuerpo):
        self.__mensaje.append(Mensaje(destinatario, remitente, asunto, cuerpo))
    def ListarMensajes(self):
        if not self.__mensaje:
            print(f"La carpeta {self.nombre} de {self.propietario.nombre} esta vacia")
        else:
            print(f"{self.propietario.nombre} en la carpeta {self.nombre} tiene los siguientes mensajes:")
            for m in self.__mensaje:
                print(m)
    def EliminarMensaje(self, id_mensaje):
        for mensaje in self.__mensaje:
            if mensaje.id == id_mensaje:
                self.__mensaje.remove(mensaje)