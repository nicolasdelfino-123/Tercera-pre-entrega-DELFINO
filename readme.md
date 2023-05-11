### Tercera-pre-entrega-DELFINO
# proyecto_perros

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
+ Acceder a la página
```
127.0.0.1:8000
```
# El proyecto cuenta con las siguientes rutas
+ crear_perro
+ listar_perros
+ crear_adoptante
+ listar_adoptantes
+ crear_adopcion
+ listar_adopcion
+ buscar_perro

## Acerca del proyecto
+ El proyecto es una página para la creación de adoptantes y la adopción de perros por tamaño (chico, mediano y grande)
+ Al ingresar a la página usted verá una lista de perros con su fecha de ingreso al canil para adopción, su nombre y tamaño.
+ Desde allí podrá crear un perro nuevo o buscarlos por tamaño a los que ya han sido creados.
+ Si selecciona Agregar perro le saldrá el formulario para Agregarlo, una vez agregado lo redireccionará a la lista de perros.
+ Si selecciona el otro campo Buscar perro por tamaño debe ingresar (chico,mediano o grande) y le filtrará en 
la lista los perros para adoptar según el tamaño que haya seleccionado.
+ El otro apartado en la página es Adoptantes donde le muestra los adoptantes o podrá crear un nuevo adopatante.
+ Finalmente está el link hacia adopciones donde usted podrá acceder para adoptar un perro.