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
# despues se va a completar
#    def CrearCarpeta(self, Nombre1):
#        for carpeta in self.__carpetas:
#            if carpeta.nombre == Nombre1:
#                print(f"La carpeta {carpeta.nombre} ya existe. Intente denuevo.")
#                return
#            nueva_carpeta = Carpeta(self.nombre, Nombre1)
#            self.__carpetas.append(nueva_carpeta)

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


class Mensaje:
    id_clase = 0
    def __init__(self, destinatario, remitente, asunto, cuerpo):
        Mensaje.id_clase +=1
        self.id=Mensaje.id_clase
        self.destinatario=destinatario
        self.remitente=remitente
        self.asunto=asunto
        self.cuerpo=cuerpo
#mensaje por defecto al llamar al objeto
    def __str__ (self):
        return f"De: {self.remitente}, Para: {self.destinatario}, Asunto: {self.asunto}, Id: {self.id}"

#llamada a metodos
servidor=ServidorCorreo()
servidor._MostrarUsuario()
servidor._MostrarCarpeta()
Camila=servidor.get_usuario("Camila")
Jorge=servidor.get_usuario("Jorge")
Camila.RedactarMensaje("Jorge", "Hola", "Mundo")
Camila.RedactarMensaje("Jorge", "gustos", "me gusta la pizza")
Camila.ListarMensajes("Borrador")
Camila.EnviarMensajes(2)
Jorge.ListarMensajes("Bandeja de entrada")
Camila.ListarMensajes("Enviados")
Camila.ListarMensajes("Borrador")