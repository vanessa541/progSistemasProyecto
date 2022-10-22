# progSistemasHilos
### Introducción (problema a resolver): En una sucursal de venta de peliculas en DVD les interesa tener un buscardor particular en donde puedan cosultar distintas peliculas, saber su sinopsis, los actores que salen en la pelicula y poder visualizar el poster de la misma. Desean visulaizar la información en una interfaz gráfica.

## Metodologia 
### Programación concurrente
#### Se conoce por programación concurrente a la rama de la informática que trata de las técnicas de programación que se usan para expresar el paralelismo entre tareas y para resolver los problemas de comunicación y sincronización entre procesos. El principal problema de la programación concurrente corresponde a no saber en que orden se ejecutan los programas (en especial los programas que se comunican). Se debe tener especial cuidado en que este orden no afecte el resultado de los programas.
### Hilos
#### Un hilo (en inglés “thread”) es la menor de las estructuras lógicas de programación que se ejecuta de forma secuencial por parte del planificador del S.O.
#### Un hilo es un proceso del sistema operativo con características distintas de las de un proceso normal:
#### Los hilos existen como subconjuntos de los procesos.
#### Los hilos comparten memoria y recursos.
#### Los hilos ocupan una dirección diferente en la memoria
#### En Python 2.X se pueden crear hilos utilizando el módulo threads y en Python 3.X se pueden crear utilizando el módulo _threads. El módulo threading será utilizado para interactuar con el módulo _threads.
### ¿Cuando implementar hilos? Cuando se quiera ejecutar una función al mismo tiempo que se ejecuta un programa. Cuando se crea software para servidores se quiere que el servidor no reciba solo una sino múltiples conexiones. Los hilos permiten completar varias tareas al mismo tiempo.
### Adjunto enlace que lleva a la definicion de las funciones del modulo threading en phyton: https://docs.python.org/es/3/library/threading.html 

## Comienzo de la interfaz gráfica....
#### Comence dibujando como queria que se viera mi interfaz gráfica, teniendo un boceto de ella.
![D70FE955-7323-4704-87FD-66C252766062](https://user-images.githubusercontent.com/111407329/196535174-87eb9ef6-1d03-4331-91af-f04787adff46.jpeg)

#### La primera implementación de la interfaz gráfica esta lista, el gridLayout no es visible ya que falta la busqueda del servidor.
<img width="390" alt="image" src="https://user-images.githubusercontent.com/111407329/196537529-752c8baf-6359-414a-92de-b42f3db31e43.png">

#### En la siguiente captura es visible como logre agregar un poster de pelicula, de forma directa, aun me falta, implementar la busqueda.
<img width="439" alt="image" src="https://user-images.githubusercontent.com/111407329/196538232-01df1528-5a36-4362-ae6a-c509e0b1d1c8.png">


