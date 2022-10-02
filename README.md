Proyecto creado en septiembre de 2022, en el marco del curso de CoderHouse de Python (framework Django).

Nombre del proyecto:
ArteBio: paredes que hablan, ciudades que dicen.

Descripción del proyecto:
El proyecto en formato blog tiene por intención que los usuarios registrados puedan interactuar con posteos propios o ajenos, relacionados con obras artísticas de contenido "naturaleza" (específicamente graffitis o murales) asociados a la ciudad a la que pertenecen y datos afines. 
Cada posteo se destacará en su sección luciendo la siguiente información: Ciudad, País, Fecha de la fotografía, Autor de la fotografía y Descripción, pensado como un espacio para darle un marco contextual a la foto, con un espacio acotado a doscientos caracteres.

La temática general se subdivide en tres secciones:

* INTERACCIONES: obras que integren humanos con animales/plantas.
* ANIMALES.
* PLANTAS.

Link de video explicado: 
https://www.loom.com/share/8e529a81171f41a384985f452c19d4b2 (Parte 1/2= 5 minutos)
https://www.loom.com/share/9d0e24e8afd249cb8e4af247e756853c (Parte 2/2= 2.34 minutos)

Composición del proyecto:
El proyecto se compone de una única aplicación en la cual se integran los archivos fundamentales.

* Models.py:
En este archivo se encuentra el desarrollo de los modelos de datos usados en el backend (interacciones, animales, plantas, avatar).
* Forms.py:
En este archivo se encuentran las estructuras de formularios utilizados para los posteos de las tres secciones de la app, para el usuario y su avatar.
* Urls.py:
Contiene las rutas de navegabilidad de la aplicación, estructuradas por modelos.
* Views.py:
Contiene la lógica de la aplicación, en forma de funciones y clases, interactuando entre la base de datos y las plantillas. 
Acá se procesa básicamente el CRUD (create, read, update y delete) de las tres secciones de la app, la lógica relacionada al registro, login, logout y avatar del usuario.
* Templates/app_agenda.py: 
En esta carpeta se encuentran los archivos .html. Se ha comenzado con una plantilla base prediseñada para la página de inicio y modificada posteriormente a conveniencia. Luego, utilizando el concepto de herencia de templates, se mantuvo una estética uniforme en las plantillas sucesivas, conservando encabezado y zócalo.
En cada una de las vistas de cada pantalla luce: * Acerca de mi: una foto personal y un párrafo de presentación.
Contacto: mi email personal.
Redes: al no contar la aplicación con redes vigentes, los íconos están asociados a cuentas personales o afines.

Algunas consideraciones:
Solo los usuarios registrados y logueados podrán acceder al material de la página.


Creador: R Cristian Saccani.
DNI. 32.195.869
