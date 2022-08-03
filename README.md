# ProyectoCoder

# Integrantes
Ana Balbi
Andrés Convertini

# Indicaciones para iniciar
Crear un entorno virtual con venv
python -m venv "nombre del entorno"
"nombre del entorno"\Scripts\activate
pip install django

# Idea de la aplicación
El principio es armar un sitio donde un cliente pueda tener asociado discos con canciones que adquirió de un listado de discos disponibles. L intención es buscar discos por genero o por nombre y que al comprarlos el cliente tenga asociado el disco que adquirió.

# About us
******
Andrés Convertini
25/07/2022
Versión 00
******
Para navegar a la página de about us simplemente dirigirse a /about/

# App Artistas
******
Andrés Convertini
31/07/2022
Versión 03
******

1) Listar todos los artistas desde la url localhost/artistas/. Login no es requerido
2) Listar todas las bandas desde la url localhost/bandas/
2) Cargar un nuevo artista desde la url localhost/artistas/alta/ o dar click en el botón 'Agregar Artista'
3) Cargar una nueva banda desde la url localhost/artistas/alta_banda/

## Edición de un artista
1) Para ver mas información del artista clickear en detalle donde lo llevará a la información del artista
2) Para editar al artista dar click en Actualizar información en la pestaña de detalle del artista
3) 

Para ello el usuario debe estar registrado

# App Discos
Todavía no se encuentra funcional

# App Usuarios
******
Andrés Convertini
19/07/2022
Versión 00
******
Hasta ahora se permite:
1) Iniciar sesión mediante el boton Login
2) Darse de alta desde el boton Sign up
3) Cerrar sesión desde el boton Log Out

## Función Mensajes 

******
Andrés Convertini
31/07/2022
Versión 02
******

Esta funcionalidad pertenece a la app de usuarios y permite establecer un chat entre usuarios de la aplicación

Condiciones:
1) Debemos estar logueados
2) Debe haber como mínimo dos usuarios en la aplicación registados ya que el char funciona entre dos usuarios

Descripción del funcionamiento:
Para ir a la aplicación de mensajería solo basta con clickear el boton Mensajes en la barra de navegación o bien /usr/messenger/

De no haber hilos abiertos (entiendase por hilo a una conversación entre dos usuarios) le permitirá crear un nuevo hilo mediante el botón nuevo mensaje. Este botón lo llevará a una página intermedia donde deberá indicar el destinatario del mensaje.

Una vez decidido el destinatario con el botón nuevo mensaje podrá dirigirse al panel de mensajes donde podrá empezar la conversación. En caso de que usted genere un nuevo mensaje con un usuario con el cual ya haya tenido una conversación el aplicativo lo llevará al hilo correspondiente sin crear nuevos hilos.

Para enviar un nuevo mensaje solo debe escribir el mismo en el campo body y pulsar el botón enviar.

Tests:
En el archivo test.py de la app se generaron algunos de los test unitarios para este modulo. Para ejecutarlos ejecutar python manage.py test


# TESTS
Los test unitarios si existen se encuentran cargados sobre cada app. En la carpeta test pueden verse en un excel los test cargados.

# Data inicial
******
Andrés Convertini
02/08/2022
Versión 00
******
Andres Convertini
Si lo desea puede importar algunos datos iniciales para testar algunas funcionalidades.
Para realizar este import debe:
1) Iniciar la consola de django mediante el comando python manage.py shell
2) Importar la librería base 
from Base.initial import *
3) Ejecutar las funciones en el orden que se detallan:
* crear_bandas()
* crear_generos()
* crear_artistas_coldplay()
* crear_discos_coldplay()




