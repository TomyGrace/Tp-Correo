
from MainCarpeta import Carpeta
from MainMensaje import Mensaje
from Interfaz import carpeta_abstracta

class Usuario(carpeta_abstracta):
    def __init__ (self, nombre, contraseña, servidor):
        self.nombre=nombre
        self.__contraseña=contraseña
#puntero al servidor al cual pertenece el usuario
        self.servidor=servidor
        self.__carpetas=[
            Carpeta(self, "Bandeja de entrada"),
            Carpeta(self, "Enviados"),
            Carpeta(self, "Borrador"),
            Carpeta(self, "Papelera"),
        ]
#para acceder a __contraseña
    def __get_contraseña(self):
        return self.__contraseña
# para devolver la informacion del usuario
    def __informacion(self):
        return f"Usuario({self.nombre}, Contraseña: {self.__get_contraseña()})"
    def devolver_info(self):
        return self.__informacion()
#para devolver la lista entera de carpetas (falta trabajo)
    def devolver_lista_carpetas(self):
        return self.__carpetas
    def __get_carpeta(self):
        return [carpeta.nombre for carpeta in self.__carpetas]
    def devolver_carpetas(self):
        return self.__get_carpeta()
# el usuario activa los siguientes 4 metodos
    def RedactarMensaje(self, destinatario, asunto, cuerpo):
        self.servidor.RedactarMensaje(destinatario, asunto, cuerpo, self.nombre)
    def EnviarMensajes(self, id_mensaje):
        for carpeta in self.__carpetas:
            if carpeta.nombre == "Borrador":
                carpeta.EnviarMensajes(id_mensaje)
                carpeta.EliminarMensaje(id_mensaje)

    def RecibirMensajes(self, mensaje):
        for carpeta in self.__carpetas:
            if carpeta.nombre == "Bandeja de entrada":
                carpeta.RecibirMensajes(mensaje)
    def mover_a_enviados(self, mensaje):
        for carpeta in self.__carpetas:
            if carpeta.nombre == "Enviados":
                carpeta.RecibirMensajes(mensaje)
    def ListarMensajes(self, carpeta):
        self.servidor.ListarMensajes(carpeta, self.nombre)