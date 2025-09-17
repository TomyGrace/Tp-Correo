from abc import ABC, abstractmethod

class carpeta_abstracta (ABC):
    @abstractmethod
    def EnviarMensajes(self):
        pass
    @abstractmethod
    def RecibirMensajes(self):
        pass
    @abstractmethod
    def ListarMensajes(self):
        pass



class ServidorCorreo:
    def __init__ (self):
        self.__usuarios={
            "Camila": Usuario("Camila", "abcd"),
            "Jorge": Usuario("Jorge", "1234"),
        }
    def _MostrarUsuario (self):
        for nombre, usuario in self.__usuarios.items():
            print(usuario.devolver_info())

class Usuario:
    def __init__ (self, nombre, contraseña):
        self.nombre=nombre
        self.__contraseña=contraseña
    def __get_contraseña(self):
        return self.__contraseña
    def __informacion(self):
        return f"Usuario({self.nombre})"
    def devolver_info(self):
        return self.__informacion()

class Carpeta(carpeta_abstracta):
    def __init__(self, propietario, nombre, mensaje):
        self.propietario=propietario
        self.nombre=nombre
        self.mensaje=mensaje
    def EnviarMensajes(self):
        pass
    def RecibirMensajes(self):
        pass
    def ListarMensajes(self):
        pass

class Mensaje:
    def __init__(self, destinatario, remitente, asunto, cuerpo, id):
        self.destinatario=destinatario
        self.remitente=remitente
        self.asunto=asunto
        self.cuerpo=cuerpo
        self.__id=id


servidor=ServidorCorreo()
servidor._MostrarUsuario()