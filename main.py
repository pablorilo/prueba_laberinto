from labyrinth import Labyrinth

def main():
    # Definimos el laberinto representado como una matriz de caracteres
    lab = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    # Creamos una instancia de la clase Labyrinth con el laberinto dado
    labyrinth = Labyrinth(lab)

    # Llamamos al método move() para encontrar el camino en el laberinto
    labyrinth.move()

if __name__ == "__main__":
    main()