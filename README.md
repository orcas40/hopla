# hopla
technical test

***
## Description
***
Prueba Backend Developer

Requisitos
Se debe desarrollar con las tecnologías Django y Postgresql y las librerías externas a convenir.

Proyecto: Gestión de tickets

Crear un api rest que nos permita gestionar los tickets de creación de transacciones en una aplicación de
subida de fotos, este api tendrá los siguientes componentes:

-Un endpoint para crear un ticket para envío de fotos, al cual se le pueda indicar el número de
imágenes a subir y que permita monitorizar el estado de las mismas.

-Se debe crear otro endpoint que permita subir imágenes (una a una), hasta llegar al número de
imágenes indicadas para su creación. Estas imágenes nunca se deben guardar en el servidor,
serán enviadas a un storage de externo (ej: Cloudinary). Ver referencia:
https://cloudinary.com/documentation/admin_api
NOTA: esta tarea se debe realizar en background (se recomienda utilizar celery aunque es a
convenir).

-Una vez el ticket recibe todas las imágenes que se ha indicado en su creación, este debe
pasar a un estado de completado.

-Para que el sistema permita crear un ticket este debe antes tener autenticación por token y
así asociar el usuario de django al ticket.

-Se debe crear un endpoint que permita ver todos los tickets paginados (es decir por usuario
autenticado), además se debe poder filtrar por rango de fecha y estado.

-Se debe crear un endpoint donde se pueda ver el detalle de un ticket, si se tiene acceso al
mismo.
Nota: El sistema no debe permitir ni eliminar ni actualizar un ticket a través del api rest. Estas
operaciones solo estarán disponibles desde el panel administrativo de Django

***
## Notas:
***
*** 
## En lugar de usar Postgresql use db.sqlite3
***
## adjunto se agrego el venv para usar python 3.9
***

***
## Installation
***
Pasos para instalar y ejecutar el projecto.
```

$ git clone https://github.com/orcas40/hopla.git
$ cd hopla
$ source myenv/bin/activate
$ cd hoplaProject
$ python manage.py runserver
```

***
## Usuario : colvera , Password : todosepuede
***

***
## Probar en Postman
***
Se comparte el archivo json con la coleccion de requests en la ruta : 
```


hopla/Hopla.postman_collection.json
```


