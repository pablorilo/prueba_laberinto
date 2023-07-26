from box import Box

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
            return row + 2 <= len(self.labyrinth)-1 and \
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

  def get_next_moves(self,row, column, position):
    # Retorna una lista con todas las direcciones válidas a las que se puede mover
    valid_moves = []
    for direction in ['right', 'down' , 'rotation', 'up', 'left']:
      if self.can_move(row, column, direction):
        valid_moves.append(direction)
    return valid_moves
  

  def explore(self, row, column, position, path, visited_cells):
    # Función recursiva para explorar todas las opciones válidas y almacenar el camino en path
    valid_moves = visited_cells[(row, column, position)]
        
    if (row, column, position) == (self.final[0], self.final[1], 'V'):
        print(f"Camino encontrado: {path}")
        self.steps = len(path)
        return self.steps

    if len(valid_moves) == 0:
        print("Sin movimientos disponibles. Retrocediendo...")
        return False

    for direction in valid_moves.copy():  # Usamos copy() para iterar sobre una copia de la lista
    
        new_row, new_column, new_position  = row, column, position
    
        if direction == 'up':
          entry = 'down'
          new_row -= 1
        elif direction == 'down':
          entry = 'up'
          new_row += 1
        elif direction == 'right':
          entry = 'left'
          new_column += 1
        elif direction == 'left':
          entry = 'right'
          new_column -= 1
        elif direction == 'rotation':
          entry = 'rotation'
          new_position = 'V' if new_position == 'H' else 'H'
            
        valid_moves.remove(direction)
        if (new_row, new_column, new_position) not in path:
          path.append((new_row, new_column, new_position))
          new_valid_moves = self.get_next_moves(new_row, new_column, new_position)
          new_valid_moves.remove(entry)
          visited_cells[(new_row, new_column, new_position)] = new_valid_moves
          step = self.explore(new_row, new_column, new_position, path, visited_cells)
          if not isinstance(step, int):
             print(f"El número de pasos para salir del laberinto es {step}")
          if step:
            return True
          else:
            # Si no se encontró un camino, deshacemos el movimiento actual buscando que haya movimientos en la celda anterior, si no sigue buscando
            while path and visited_cells[path[-1]]== []:
              path.pop()          
            row = path[-1][0]
            column = path[-1][1]
            new_position = path[-1][2]

    return False
    
  
  def move(self):
        # Llama a la función explore() con la posición inicial y otros parámetros
        path = [(self.box.row, self.box.column, self.position)]  # Lista para almacenar el camino
        valid_moves = self.get_next_moves(self.box.row, self.box.column, self.position)
        visited_cells = {(self.box.row, self.box.column, self.position): valid_moves}  # dict para almacenar las celdas visitadas
        self.explore(self.box.row, self.box.column, self.position, path, visited_cells)