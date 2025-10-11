from MainServidor import ServidorCorreo
from MainUsuario import Usuario
from MainCarpeta import Carpeta
from MainMensaje import Mensaje


# despues se va a completar
#    def CrearCarpeta(self, Nombre1):
#        for carpeta in self.__carpetas:
#            if carpeta.nombre == Nombre1:
#                print(f"La carpeta {carpeta.nombre} ya existe. Intente denuevo.")
#                return
#            nueva_carpeta = Carpeta(self.nombre, Nombre1)
#            self.__carpetas.append(nueva_carpeta)

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
Camila.Buscar_Subcarpeta("Bandeja de entrada")