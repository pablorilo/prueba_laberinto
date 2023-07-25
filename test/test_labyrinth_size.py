import pytest

from labyrinth import Labyrinth


# Test para verificar que el método check_labyrinth_size devuelve el resultado esperado para diferentes laberintos
@pytest.mark.parametrize("lab, expected_result", [
    ([
        ['.', '.', '.'],
        ['.', '#', '.'],
        ['.', '.', '.']
    ], True),  # Laberinto válido
    ([
        ['.', '.', '.'],
        ['.', '#', '.']
    ], False),  # Laberinto con menos de 3 filas
    ([
        ['.', '.'],
        ['.', '#'],
        ['.', '.'],
        ['.', '.']
    ], False),  # Laberinto con menos de 3 columnas
    ([
        ['.', '.', '.'],
        ['.', '#', '.'],
        ['.', '.']
    ], False)  # Laberinto con filas de diferentes tamaños
])
def test_check_labyrinth_size(lab, expected_result):
    labyrinth = Labyrinth(lab)
    assert labyrinth.check_labyrinth_size() == expected_result
