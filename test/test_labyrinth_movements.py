import pytest
from labyrinth import Labyrinth, Box

# Definición de la fixture(permiten datos o configuraciones que se pueden reutilizar en múltiples pruebas.) 'labyrinth' que crea una instancia de la clase Labyrinth con un laberinto predefinido.
@pytest.fixture
def labyrinth():
    lab = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
    ]
    return Labyrinth(lab)

def test_can_move(labyrinth):
    # Prueba para una posición válida en la parte superior izquierda del laberinto
    assert labyrinth.can_move(0, 0, 'right') == True
    assert labyrinth.can_move(0, 0, 'down') == False
    assert labyrinth.can_move(0, 0, 'left') == False
    assert labyrinth.can_move(0, 0, 'up') == False
    assert labyrinth.can_move(0, 0, 'rotation') == False

    # Prueba para una posición válida en el centro del laberinto (orientación H)
    labyrinth.box.orientation = 'H'
    assert labyrinth.can_move(2, 2, 'right') == True
    assert labyrinth.can_move(2, 2, 'down') == False
    assert labyrinth.can_move(2, 2, 'left') == True
    assert labyrinth.can_move(2, 2, 'up') == False
    assert labyrinth.can_move(2, 2, 'rotation') == False

    # Prueba para una posición válida en el centro del laberinto (orientación V)
    labyrinth.box.orientation = 'V'
    assert labyrinth.can_move(2, 0, 'right') == False
    assert labyrinth.can_move(2, 0, 'down') == True
    assert labyrinth.can_move(2, 0, 'left') == False
    assert labyrinth.can_move(2, 0, 'up') == True
    assert labyrinth.can_move(2, 0, 'rotation') == False

    # Prueba para una posición válida en la parte inferior derecha del laberinto
    labyrinth.box.orientation = 'H'
    assert labyrinth.can_move(4, 4, 'right') == False
    assert labyrinth.can_move(4, 4, 'down') == False
    assert labyrinth.can_move(4, 4, 'left') == True
    assert labyrinth.can_move(4, 4, 'up') == False
    assert labyrinth.can_move(4, 4, 'rotation') == False

  
