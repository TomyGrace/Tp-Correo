class ServidorCorreo:
    def __init__ (self, nombre):
        self.nombre=nombre
        self.__usuarios=
        self.__registros=

class Usuario:
    def __init__ (self, nombre, correo, contraseña):
        self.nombre=nombre
        self.correo=correo
        self.__contraseña=contraseña

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