class Box:
  def __init__(self,  row , column, orientation):
    """
        Constructor de la clase Box que genera la barra.

        Parámetros:
        - row (int): La fila de la celda de referencia del objeto.
        - column (int): La columna de la celda de referencia del objeto.
        - orientation (str): La orientación del objeto ('H' para horizontal, 'V' para vertical).
    """
    self.column = column
    self.row = row
    self.orientation = orientation

  def get_orientation(self):
      """
        Obtiene la orientación actual del objeto.

        Retorna:
        str: La orientación actual del objeto ('H' para horizontal, 'V' para vertical).
      """
      return self.orientation


class Labyrinth:
  def __init__(self,lab):
    """
        Constructor de la clase Labyrinth.

        Parámetros:
        - lab (list): Laberinto representado como una lista de listas.
    """
    self.labyrinth = lab
    self.start = [0,1]
    self.final = [len(lab)-2, len(lab[0])-1]  # obtenemos la posición de salida de la celda central
    self.position = 'H' #posicion horizontal
    self.box = Box(self.start[0], self.start[1], self.position)
    self.way = []
    self.visited_cells = {} 
    
    
  def check_labyrinth_size(self):
        # Verificar tamaño de la matriz principal
        rows = len(self.labyrinth)
        if not (3 <= rows <= 1000):
            return False

        columns = len(self.labyrinth[0])
        if not (3 <= columns <= 1000):
            return False

        # Verificar tamaño de todas las filas del laberinto
        for row in self.labyrinth:
            if len(row) != columns:
                return False

        return True
