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
    def Buscar_Subcarpetas(self, usuario, nombre):
        for n in self._usuarios.values():
            if n == usuario:
                for c in n.devolver_lista_carpetas():
                    Carpeta=c.BuscarSubcarpeta(nombre)
                    if Carpeta is not None:
                        return Carpeta
                return None
    def Buscar_Mensaje(self, asunto, remitente, usuario):
        for u in self._usuarios.values():
            if u == usuario:
                for c in u.devolver_lista_carpetas():
                    resultado = c.BuscarMensaje(asunto, remitente)
                    if resultado:
                        return resultado
                return None
    def MoverMensaje(self, mensaje, origen, destino, usuario):
        for u in self._usuarios.values():
            if u == usuario:
                if isinstance(origen, Carpeta):
                    carpeta_origen=origen
                else:
                    carpeta_origen=None
                    for c in u.devolver_lista_carpetas():
                        carpeta_origen=c.BuscarSubcarpeta(origen)
                        if carpeta_origen:
                            break
                if isinstance(destino, Carpeta):
                    carpeta_destino=destino
                else:
                    carpeta_destino=None
                    for c in u.devolver_lista_carpetas():
                        carpeta_destino=c.BuscarSubcarpeta(destino)
                        if carpeta_destino:
                            break
                if carpeta_destino is None or carpeta_origen is None:
                    print("No se encontro la carpeta origen o destino. Revise los parametros")
                    return
                carpeta_destino.RecibirMensajes(mensaje)
                carpeta_origen.EliminarMensaje(mensaje.id)
                return
    def AgregarCarpeta(self, nombre, usuario):
        for u in self._usuarios.values():
            if u == usuario:
                for c in u.devolver_lista_carpetas():
                    if c == nombre:
                        return print("La carpeta ya existe")
        u.CrearCarpeta(nombre)