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
  
  def move(self):
    print("\n####################### Comprobando dimensiones del laberinto #################################")
    # Llamar a la función explore() con la posición inicial y otros parámetros, primeramente comprobamos si el laberinto cumple con las condiciones de forma
    if self.check_labyrinth_size():
        print("\n[INFO] Laberinto correcto")
        path = []  # Lista para almacenar el camino
        visited_cells = set()  # Conjunto para almacenar las celdas visitadas
        print("[INFO] Iniciando pruebas\n")
        if self.explore(self.start[0], self.start[1], self.position, path, visited_cells):
            # Verificar si el camino llega a la posición final
            if path[-1][0:2] == tuple(self.final):
                print(f"Camino encontrado, numero de pasos: {len(path)}")
                print(path)
                return True

        print("Camino no encontrado.")
        return False

  def explore(self, row, column, position, path, visited_cells):
    # Verifica si la posición actual ya ha sido visitada antes.
    if (row, column, position) in visited_cells:
        return False

    # Verifica si la posición actual coincide con la posición final y si el objeto está en posición vertical ('V').
    if (row, column) == tuple(self.final) and position == 'V':
        # Si se ha alcanzado el estado final y el objeto está en posición vertical, agrega la posición actual al camino y finaliza la exploración.
        path.append((row, column, position))
        return True

    # Explora todas las direcciones posibles desde la posición actual.
    for direction in self.get_next_moves(row, column, position):
        # Inicializa las nuevas coordenadas y la nueva posición del objeto según la dirección actual.
        new_row, new_column, new_position = row, column, position

        # Calcula las nuevas coordenadas y posición del objeto según la dirección actual.
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
            # Realiza la rotación del objeto cambiando su posición de horizontal a vertical o viceversa.
            new_position = 'V' if new_position == 'H' else 'H'

        # Agrega la posición actual al camino y marca la celda como visitada.
        path.append((row, column, position))
        print(path)
        visited_cells.add((row, column, position))

        # Verifica si es posible moverse a la nueva posición.
        if self.can_move(new_row, new_column, entry):
            # Si es posible, realiza la exploración desde la nueva posición y posición del objeto.
            if self.explore(new_row, new_column, new_position, path, visited_cells):
                return True
        else:
            # Si no es posible moverse, retrocede eliminando la posición actual del camino.
            path.pop()

    # Si no se encontró una solución en ninguna de las direcciones, retorna False.
    return False

  