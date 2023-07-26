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
  
  def get_occupied_cells(self):
        # Retorna las celdas ocupadas por el objeto en función de su orientación
        if self.orientation == 'H':
            return [(self.row, self.column), (self.row, self.column - 1), (self.row, self.column + 1)]
        elif self.orientation == 'V':
            return [(self.row, self.column), (self.row - 1, self.column), (self.row + 1, self.column)]
