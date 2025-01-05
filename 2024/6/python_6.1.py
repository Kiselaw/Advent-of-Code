def get_guard_position(matrix: list[str]) -> tuple:
    guard_position: tuple = tuple()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                guard_position = (i, j)
    return guard_position


def solution(matrix: list[str]) -> int:
    counter = set()
    i, j = get_guard_position(matrix)
    counter.add((i, j))
    direction = 1
    while all([i != len(matrix) - 1, j != len(matrix[0]) - 1, i != 0, j != 0]):
        if direction == 1:
            obstacle = True if matrix[i - 1][j] == "#" else False
            if not obstacle:
                counter.add((i - 1, j))
                i -= 1
            else:
                direction += 1
                continue
        elif direction == 2:
            obstacle = True if matrix[i][j + 1] == "#" else False
            if not obstacle:
                counter.add((i, j + 1))
                j += 1
            else:
                direction += 1
                continue
        elif direction == 3:
            obstacle = True if matrix[i + 1][j] == "#" else False
            if not obstacle:
                counter.add((i + 1, j))
                i += 1
            else:
                direction += 1
                continue
        elif direction == 4:
            obstacle = True if matrix[i][j - 1] == "#" else False
            if not obstacle:
                counter.add((i, j - 1))
                j -= 1
            else:
                direction = 1
                continue
    return len(counter)


if __name__ == "__main__":
    matrix: list[str] = []
    with open("puzzle.txt", "r") as file:
        matrix.extend(line.strip() for line in file)
    print(solution(matrix))
