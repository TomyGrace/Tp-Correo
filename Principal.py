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



class ServidorCorreo(carpeta_abstracta):
    def __init__ (self):
        self.__usuarios={
            "Camila": Usuario("Camila", "abcd"),
            "Jorge": Usuario("Jorge", "1234"),
        }
    def _MostrarUsuario (self):
        for usuario in self.__usuarios.values():
            print(usuario.devolver_info())
    def _MostrarCarpeta(self):
        for usuario in self.__usuarios.values():
            print(usuario.devolver_carpetas())
    def EnviarMensajes(self):
        pass
    def RecibirMensajes(self):
        pass
    def ListarMensajes(self):
        pass

class Usuario(carpeta_abstracta):
    def __init__ (self, nombre, contraseña):
        self.nombre=nombre
        self.__contraseña=contraseña
        self.__carpetas=[

        ]
    def __get_contraseña(self):
        return self.__contraseña
    def __informacion(self):
        return f"Usuario({self.nombre})"
    def __get_carpeta(self):
        return self.__carpetas
    def devolver_info(self):
        return self.__informacion()
    def devolver_carpetas(self):
        return self.__get_carpeta()
    def EnviarMensajes(self):
        pass
    def RecibirMensajes(self):
        pass
    def ListarMensajes(self):
        pass
    def CrearCarpeta(self, Nombre):
        self.__carpetas.append(
            Nombre=Carpeta("self.nombre", f"{Nombre}")
            )
        

class Carpeta(carpeta_abstracta):
    def __init__(self, propietario, nombre):
        self.propietario=propietario
        self.nombre=nombre
        self.mensaje={

        }
    def EnviarMensajes(self):
        pass
    def RecibirMensajes(self):
        pass
    def ListarMensajes(self):
        pass

class Mensaje:
    def __init__(self, destinatario, remitente, asunto, cuerpo):
        self.destinatario=destinatario
        self.remitente=remitente
        self.asunto=asunto
        self.cuerpo=cuerpo
    

servidor=ServidorCorreo()
servidor._MostrarUsuario()
servidor._MostrarCarpeta()