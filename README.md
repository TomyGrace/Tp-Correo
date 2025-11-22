Descripción del proyecto



Este proyecto implementa un cliente de correo electrónico básico utilizando Python, como parte de un trabajo práctico de Programación Orientada a Objetos.

El sistema permite redactar, enviar, recibir y listar mensajes, además de administrar carpetas y realizar búsquedas recursivas.



El desarrollo cubre las funcionalidades correspondientes a Etapa 1 y Etapa 2 del trabajo.



Características implementadas

Etapa 1 – Modelado



Clases principales: ServidorCorreo, Usuario, Carpeta, Mensaje



Clase abstracta carpeta\_abstracta para definir la interfaz de mensajería



Métodos principales:



Redactar mensaje



Enviar mensaje



Recibir mensaje



Listar mensajes



Encapsulamiento y uso de atributos privados



Etapa 2 – Recursividad y estructura



Árbol de carpetas por usuario con búsqueda recursiva



Búsqueda recursiva de subcarpetas



Búsqueda recursiva de mensajes por asunto y remitente



Modularización del código



Diagramas del sistema



Los diagramas se incluyen en el directorio docs/diagramas/.



diagrama\_clases\_final.png



diagrama\_arbol\_carpetas.png



diagrama\_flujo\_busqueda\_recursiva.png



diagrama\_flujo\_mensaje.png



Estructura del proyecto

/src

&nbsp;  MainServidor.py

&nbsp;  MainUsuario.py

&nbsp;  MainCarpeta.py

&nbsp;  MainMensaje.py

&nbsp;  Interfaz.py

&nbsp;  Principal.py



/docs

&nbsp;  Documentación\_Final.docx

&nbsp;  Presentación\_Proyecto\_Correo.pptx

&nbsp;  /diagramas



Cómo ejecutar



Clonar el repositorio



Ejecutar el archivo principal:



python Principal.py





Esto permite probar la creación de usuarios, el envío y recepción de mensajes, la búsqueda recursiva y la administración de carpetas.



Ejemplo de uso

servidor = ServidorCorreo()

camila = servidor.get\_usuario("Camila")



camila.RedactarMensaje("Jorge", "Hola", "Mensaje de prueba")

camila.ListarMensajes("Borrador")

camila.EnviarMensajes(1)



Funcionalidades faltantes (Etapa 3)



La consigna incluye elementos que aún no se implementaron. El diseño actual permite incorporarlos más adelante.



Pendiente de implementación:



Filtros automáticos



Mensajes urgentes mediante cola de prioridad



Red de servidores usando grafos



Interfaz de usuario más avanzada (CLI interactiva o GUI)



Cómo podrían integrarse:



Los filtros pueden gestionarse con listas y diccionarios, aplicándose al momento de recibir mensajes.



Las prioridades pueden implementarse con heapq para obtener siempre el mensaje más urgente.



La red de servidores puede representarse mediante un grafo y recorrerse con BFS o DFS.



La CLI puede construirse como menú interactivo reutilizando los métodos ya existentes.



Autor



Tomas Gracevich

