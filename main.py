from collections import deque


def busqueda_amplitud(grid, start, end):
    moves = [(0, -1, "ARRIBA"), (0, 1, "ABAJO"), (-1, 0, "IZQUIERDA"), (1, 0, "DERECHA")]
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        visited[y][x] = True

        for dx, dy, move in moves:
            new_x, new_y = x + dx, y + dy

            if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid)) and not visited[new_y][new_x] and grid[new_y][
                new_x] != 'X':
                queue.append(((new_x, new_y), path + [move]))

    return []


def displayPathtoPrincess(N, grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'p':
                princess = (j, i)
            elif grid[i][j] == 'm':
                bot = (j, i)

    moves = busqueda_amplitud(grid, bot, princess)
    return moves


def score(N, moves):
    return (N * N - len(moves)) / 10


if __name__ == "__main__":

    print("Ingrese un valor entero, positivo e impar entre 3 y 99:")
    N = int(input().strip())

    # Validación para el tamaño N
    while not (3 <= N < 100 and N % 2 == 1):
        N = int(input("Por favor, ingrese un valor entero, positivo e impar entre 3 y 99:").strip())

    grid = []
    print("Ingrese una fila válida de longitud", N)
    print("usando '-' para armar el tablero, 'm' posicion del bot, 'p' posicion de la princesa, 'X' posicion de los obstaculos): ")
    for _ in range(N):
        grid_row = input().strip()
        while len(grid_row) != N or not all(cell in ['-', 'm', 'p', 'X'] for cell in grid_row):
            grid_row = input(f"Por favor, ingrese una fila válida de longitud {N} (usando -, m, p, X):").strip()
        grid.append(grid_row)

    moves = displayPathtoPrincess(N, grid)

    if not moves:
        print("El bot no puede llegar a la princesa debido a los obstáculos.")
    else:
        for move in moves:
            print(move)
        print("Puntuación:", score(N, moves))


