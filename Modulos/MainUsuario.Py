
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
# metodos de busqueda recursiva
    def Buscar_Subcarpeta(self, nombre):
        resultado = self.servidor.Buscar_Subcarpetas(self, nombre)
        if resultado == None:
            print(f"No existe la carpeta {nombre}")
        else: 
            print(resultado.nombre)
# busca mensajes por asunto y remitente en carpetas y subcarpetas del usuario que las solicita, (recorre en preorder)
    def Buscar_Mensaje(self, asunto, remitente):
        resultado = self.servidor.Buscar_Mensaje(asunto, remitente, self)
        if resultado is not None:
            mensaje_f, carpeta_origen = resultado
            print(mensaje_f)
        else: 
            print("No existe un mensaje con ese usuario y remitente")
# mueve mensajes, necesita asunto, remitente y carpeta de destino para mover el mensaje
    def MoverMensaje(self, asunto, remitente, carpeta_destino):
        resultado = self.servidor.Buscar_Mensaje(asunto, remitente, self)
        if resultado is None:
            print("El mensaje que intenta mover no existe, revise los parametros indicados")
            return
        mensaje, ubicacion = resultado
        destino_mensaje = self.servidor.Buscar_Subcarpetas(self, carpeta_destino)
        if destino_mensaje is None:
            print(f"No existe la carpeta {destino_mensaje}. Por favor, indique otro destino")
            return
        self.servidor.MoverMensaje(mensaje, ubicacion, destino_mensaje, self)
        print(f"El mensaje se movio exitosamente a {destino_mensaje.nombre}")

    def AgregarCarpetas(self, nombre):
        self.servidor.AgregarCarpeta(nombre, self)

    def CrearCarpeta(self, nombre):
        self.__carpetas.append(Carpeta(self, nombre))