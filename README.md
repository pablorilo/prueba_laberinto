# Prueba técnica DAMAVIS
# Proyecto de Resolución de Laberintos

Este proyecto intenta implementar un programa que resuelve laberintos y encuentra la ruta más corta desde una posición de inicio hasta una posición de destino de un objeto que ocupa 3 celdas. El laberinto está representado como una matriz de celdas que pueden ser caminos '.' o paredes '#'.El objetivo es encontrar la ruta más corta desde la celda de inicio a la celda de destino, teniendo en cuenta que el objeto puede cambiar de posición y orientación en cada paso.

## Funcionalidades

Movimiento y rotación del objeto: El objeto puede moverse hacia arriba, abajo, izquierda o derecha, siempre que no encuentre una pared. Además, el objeto puede rotar 90 grados en su posición actual.

## Estructura del proyecto

```laberinto/
    ├── main.py
    ├── labyrinth.py
    ├── box.py
    └── test/
         ├── test_labyrinth_size.py
         ├── test_labyrinth_movements.py
```

**main.py**: Es el punto de entrada del programa que inicializa y ejecuta el laberinto.

**labyrinth.py**: Contiene la clase Labyrinth que representa el laberinto y sus funcionalidades.

**box.py**: Contiene la clase Box que representa el objeto en el laberinto y sus movimientos.

**test/**: Directorio que contiene las pruebas unitarias para el proyecto.

**test/test_labyrinth.py**: Archivo con pruebas unitarias para la clase Labyrinth.

## Uso del programa

1. Clona el repositorio en tu sistema local.
2. Abre una terminal o línea de comandos en la ubicación del repositorio clonado.
3. Crear entorno virtual e instalar dependencias: 
    En el proyecto consta  de un requirements.txt con las dependencias necesarias para ejecutar el programa, para instaslar dichas dependencias ejecutaremos los siguientes comandos en el terminal dentro de la carpeta del proyecto

    Creamos un entorno virual:
    * En Windows:

    ```python -m venv labenv```

    * En macOS y Linux::

    ```python3 -m venv myenv```

    Activamos el entorno 
    * En Windows:

    ```labenv\Scripts\activate```

    * En macOS y Linux:

    ```source myenv/bin/activate```

    Volvemos a la carpeta raiz ejecutando dos veces cd..

    Con el entorno virtual activado instalamos las dependencias.

    ```pip install -r requirements.txt```
       

4. En el fichero main.py introduce el laberinto
5. Ejecuta el programa con el siguiente comando:

```python main.py```



