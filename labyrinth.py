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

  
  def can_move(self, row, column, direction):
      #Verifica si la barra puede moverse en una dirección específica desde una celda dada. 
      # La función recibe la fila y columna actual de la barra y la dirección a verificar
      if direction == 'up':
        if self.box.get_orientation() == 'H':
            return 0 <= row - 1 and \
                  self.labyrinth[row - 1][column + 1] == '.' and \
                  self.labyrinth[row - 1][column] == '.' and \
                  self.labyrinth[row - 1][column - 1] == '.'
        if self.box.get_orientation() == 'V':
            return 0 <= row - 2 and \
                  self.labyrinth[row - 2][column] == '.'

      if direction == 'down':
        if self.box.get_orientation() == 'H':
            return row + 1 <= len(self.labyrinth)-1 and \
                  self.labyrinth[row + 1][column + 1] == '.' and \
                  self.labyrinth[row + 1][column] == '.' and \
                  self.labyrinth[row + 1][column - 1] == '.'
        if self.box.get_orientation() == 'V':
            return row + 2 < len(self.labyrinth)-1 and \
                  self.labyrinth[row + 2][column] == '.'

      if direction == "right":
        if self.box.get_orientation() == 'H':
            return column + 2 <= len(self.labyrinth[0])-1 and \
                  self.labyrinth[row][column + 2] == '.'
        if self.box.get_orientation() == 'V':
            return column + 1 <= len(self.labyrinth[0])-1 and \
                  self.labyrinth[row - 1][column + 1] == '.' and \
                  self.labyrinth[row][column + 1] == '.' and \
                  self.labyrinth[row + 1][column + 1] == '.'

      if direction == "left":
        if self.box.get_orientation() == 'H':
            return 0 <= column - 2 and \
                  self.labyrinth[row][column - 2] == '.'
        if self.box.get_orientation() == 'V':
            return 0 <= column - 1 and \
                  self.labyrinth[row - 1][column - 1] == '.' and \
                  self.labyrinth[row][column - 1] == '.' and \
                  self.labyrinth[row + 1][column - 1] == '.'
      if direction == 'rotation':
        if self.box.get_orientation() == 'H':
          return 0 <= row - 1 and \
                row + 1 <= len(self.labyrinth) - 1  and \
                self.labyrinth[row - 1][column] == '.' and \
                self.labyrinth[row + 1][column] == '.'
        if self.box.get_orientation() == 'V':
          return column + 1 <= len(self.labyrinth[0])-1 and \
                0 <= column - 1 and \
                self.labyrinth[row][column - 1] == '.' and \
                self.labyrinth[row][column + 1] == '.'

  