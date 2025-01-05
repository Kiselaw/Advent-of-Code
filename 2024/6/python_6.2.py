DIR = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def get_guard_starting_position(matrix: list[list[str]]) -> tuple[int, int, int]:
    guard_position: tuple[int, int, int] = (0, 0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                guard_position = (i, j, 0)
    return guard_position


def solution(matrix: list[list[str]]) -> int:
    counter = 0
    guard_position = get_guard_starting_position(matrix)
    path = move(matrix, guard_position, True)
    if isinstance(path, bool):
        return counter
    for coord in path:
        matrix[coord[0]][coord[1]] = "#"
        check = move(matrix, guard_position, False)
        if not check:
            counter += 1
        matrix[coord[0]][coord[1]] = "."
    return counter


def move(
    matrix: list[list[str]], starting_position: tuple[int, int, int], initial_path: bool
) -> set | bool:
    i, j, direction = starting_position
    path = set()
    while True:
        if initial_path:
            coord: tuple[int, int] | tuple[int, int, int] = (i, j)
        else:
            coord = (i, j, direction)
            if coord in path:
                return False
        path.add(coord)
        d_i, d_j = DIR[direction]
        if i + d_i not in range(len(matrix)) or j + d_j not in range(len(matrix[0])):
            break
        while matrix[i + d_i][j + d_j] == "#":
            direction += 1
            direction %= 4
            d_i, d_j = DIR[direction]
        i += d_i
        j += d_j
    return path


if __name__ == "__main__":
    matrix: list[list[str]] = []
    with open("puzzle.txt", "r") as file:
        matrix.extend(list(line.strip()) for line in file)
    print(solution(matrix))
