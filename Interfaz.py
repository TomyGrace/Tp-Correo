from abc import ABC, abstractmethod

#interfaz de mensajeria y listado de mensajes
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