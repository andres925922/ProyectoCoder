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
La idea es tener una página que permita ver los artistas musicales cargados, listar los discos en los que participó, las bandas en la que actualmente se desempeña e información adicional.

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
15/08/2022
Versión 04
******

1) Listar todos los artistas desde la url localhost/artistas/. Login no es requerido
2) Listar todas las bandas desde la url localhost/artistas/view_bandas
3) Cargar un nuevo artista desde la url localhost/artistas/alta/ o dar click en el botón 'Agregar Artista'
4) Cargar una nueva banda desde la url localhost/artistas/alta_banda/

## Edición de un artista
1) Para ver mas información del artista clickear en detalle donde lo llevará a la información del artista
2) Para editar al artista dar click en Actualizar información en la pestaña de detalle del artista
3) En la versión 4 de la app se permite guardar imágenes del artista y de la banda.

Para ello el usuario debe estar registrado

# Bandas
******
Andrés Convertini
15/08/2022
Versión 01
Requiere login
******

1) Listar las bandas desde la dirección /artistas/view_bandas. Esto trae todas las bandas activas en la bd
2) Actualizar bandas mediante el boton actualizar de cada uno de los box de la banda
3) Crear una nueva banda desde el botón crear una nueva banda desde la vista view_bandas
4) Eliminar una banda con el botón eliminar.
5) En la versión 1 se permite guardar imágenes de las bandas.

# App Discos
******
Andrés Convertini
15/08/2022
Versión 00
******

1) El listado de discos se encuentra en la url /
2) Sobre este listado se encuentran los botones que permiten cargar un disco, editar, borrar y ver detalles


# App Usuarios
******
Andrés Convertini
15/08/2022
Versión 01
******
Hasta ahora se permite:
1) Iniciar sesión mediante el boton Login
2) Darse de alta desde el boton Sign up
3) Cerrar sesión desde el boton Log Out
4) A partir de la versión 1 se permite editar el perfil del usuario mediante el click sobre el ícono avatar del usuario. 

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




