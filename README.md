# Prueba técnica DAMAVIS
## Proyecto de Resolución de Laberintos

Este proyecto intenta implementar un programa que resuelve laberintos y encuentra la ruta más corta desde una posición de inicio hasta una posición de destino de un objeto que ocupa 3 celdas. El laberinto está representado como una matriz de celdas que pueden ser caminos '.' o paredes '#'.El objetivo es encontrar la ruta más corta desde la celda de inicio a la celda de destino, teniendo en cuenta que el objeto puede cambiar de posición y orientación en cada paso.

### Funcionalidades

Movimiento y rotación del objeto: El objeto puede moverse hacia arriba, abajo, izquierda o derecha, siempre que no encuentre una pared. Además, el objeto puede rotar 90 grados en su posición actual.

### Estructura del proyecto

```laberinto/
    ├── main.py
    ├── labyrinth.py
    ├── box.py
    └── test/
         ├── test_labyrinth.py
```

**main.py**: Es el punto de entrada del programa que inicializa y ejecuta el laberinto.
**labyrinth.py**: Contiene la clase Labyrinth que representa el laberinto y sus funcionalidades.
**box.py**: Contiene la clase Box que representa el objeto en el laberinto y sus movimientos.
**test/**: Directorio que contiene las pruebas unitarias para el proyecto.
**test/test_labyrinth.py**: Archivo con pruebas unitarias para la clase Labyrinth.

### Requisitos del sistema

En el proyecto consta  de un requirements.txt con las dependencias necesarias para ejecutar el programa, para instaslar dichas dependencias ejecutaremos los siguientes comandos en el terminal dentro de la carpeta del proyecto
Creamos un entorno virual

 ```python -m venv labenv```

 Activamos el entorno 

 ```labenv\Scripts\activate```

 Volvemos a la carpeta raiz ejecutando dos veces cd..

 Con el entorno virtual activado instalamos las dependencias 

 ```pip install -r requirements.txt```

