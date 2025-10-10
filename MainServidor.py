from MainUsuario import Usuario
from MainCarpeta import Carpeta
from MainMensaje import Mensaje
from Interfaz import carpeta_abstracta


class ServidorCorreo(carpeta_abstracta):
    def __init__ (self):
        self._usuarios={
            "Camila": Usuario("Camila", "abcd", self),
            "Jorge": Usuario("Jorge", "1234", self),
        }
#para devolver un usuario en especifico
    def get_usuario(self,nombre):
        for usuario in self._usuarios.values():
            if usuario.nombre == nombre:
                return usuario
#para mostrar todos los usuarios
    def _MostrarUsuario (self):
        for usuario in self._usuarios.values():
            print(usuario.devolver_info())
#para mostrar las carpetas de un usuario (falta trabajo)
    def _MostrarCarpeta(self):
        for usuario in self._usuarios.values():
            print(f"Carpetas de: {usuario.nombre}, {usuario.devolver_carpetas()}")
#operaciones internas relacionadas a mensajes
    def EnviarMensajes(self, mensaje):
        self.RecibirMensajes(mensaje)
    def RecibirMensajes(self, mensaje):
        for remitente in self._usuarios.values():
            if remitente.nombre == mensaje.remitente:
                remitente.mover_a_enviados(mensaje)
        for destinatario in self._usuarios.values():
            if destinatario.nombre == mensaje.destinatario:
                destinatario.RecibirMensajes(mensaje)
    def ListarMensajes(self, carpeta, usuario):
        for k in self._usuarios.values():
            if k.nombre == usuario:
                for m in k.devolver_lista_carpetas():
                    if m.nombre == carpeta:
                        m.ListarMensajes()
    def RedactarMensaje(self, destinatario, asunto, cuerpo, Usuario):
        for k in self._usuarios.values():
            if k.nombre == Usuario:
                for m in k.devolver_lista_carpetas():
                    if m.nombre == "Borrador":
                        m.RedactarMensajes(destinatario, k.nombre, asunto, cuerpo)