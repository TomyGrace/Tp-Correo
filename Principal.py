class ServidorCorreo:
    def __init__ (self):
        self.__usuarios={
            "Camila": Usuario("Camila", "abcd"),
            "Jorge": Usuario("Jorge", "1234"),
        }
    def _MostrarUsuario (self):
        for usuario in self.__usuarios.values():
            print(usuario.devolver_info())

class Usuario:
    def __init__ (self, nombre, contraseña):
        self.nombre=nombre
        self.__contraseña=contraseña
    def get_contraseña(self):
        return self.__contraseña
    def __informacion(self):
        return f"Usuario({self.nombre}, contraseña: {self.get_contraseña()})"
    def devolver_info(self):
        return self.__informacion()

class Carpeta:
    def __init__(self, propietario, nombre, mensaje):
        self.propietario=propietario
        self.nombre=nombre
        self.mensaje=mensaje

class Mensaje:
    def __init__(self, destinatario, remitente, asunto, cuerpo, id):
        self.destinatario=destinatario
        self.remitente=remitente
        self.asunto=asunto
        self.cuerpo=cuerpo
        self.__id=id


servidor=ServidorCorreo()
servidor._MostrarUsuario()