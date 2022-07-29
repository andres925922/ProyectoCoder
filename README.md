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

# App Clientes
Hasta ahora se permite:
1) Listar todos los clientes desde la url localhost/clientes/
2) Cargar un nuevo cliente desde la url localhost/clientes/alta/
3) Listar clientes por DNI desde la url localhost/clientes/buscar_cliente_por_dni/

# App Artistas
Hasta ahora se permite:
1) Listar todos los artistas desde la url localhost/artistas/
2) Listar todas las bandas desde la url localhost/bandas/
2) Cargar un nuevo artista desde la url localhost/artistas/alta/
3) Cargar una nueva banda desde la url localhost/artistas/alta_banda/

# App Discos
Todavía no se encuentra funcional

# App Usuarios
Hasta ahora se permite:
1) Iniciar sesión mediante el boton Login
2) Darse de alta desde el boton Sign up
3) Cerrar sesión desde el boton Log Out
