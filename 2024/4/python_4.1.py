import re


def pattern_finder(string: str):
    return len(re.findall(r"(?=(XMAS|SAMX))", string))


def solution(matrix: list[str]) -> int:
    res = 0
    # count pattern in rows
    res += sum((pattern_finder("".join(row)) for row in matrix))
    # get columns and count pattern in columns
    turned_matrix = [
        [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
    ]
    res += sum((pattern_finder("".join(column)) for column in turned_matrix))
    # get diagonals and count pattern in diagonals
    max_col_len = len(matrix[0])
    max_row_len = len(matrix)
    diagonals = []
    # get forward diagonals
    for d in range(max_row_len - 1, -max_col_len - 1, -1):
        diagonal: list[str] = []
        i = max(0, d)
        j = max(0, -d)
        while True:
            if j > max_col_len - 1 or i > max_row_len - 1:
                diagonals.append(diagonal)
                break
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
    # get backwards diagonals
    for d in range(max_col_len + max_row_len - 2, -1, -1):
        diagonal = []
        i = max(0, d - max_col_len + 1)
        j = min(d, max_col_len - 1)
        while True:
            if i > max_row_len - 1 or j < 0:
                diagonals.append(diagonal)
                break
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
    # count pattern in diagonals
    res += sum((pattern_finder("".join(diagonal)) for diagonal in diagonals))
    return res


def print_diagonals(matrix):
    max_col_len = len(matrix[0])
    max_row_len = len(matrix)
    for d in range(max_row_len - 1, -max_col_len - 1, -1):
        i = max(0, d)
        j = max(0, -d)
        while True:
            if j > max_col_len - 1 or i > max_row_len - 1:
                break
            print(matrix[i][j], end="")
            i += 1
            j += 1
        print(" | ", end="")
    print()
    for d in range(max_col_len + max_row_len - 2, -1, -1):
        i = max(0, d - max_col_len + 1)
        j = min(d, max_col_len - 1)
        while True:
            if i > max_row_len - 1 or j < 0:
                break
            print(matrix[i][j], end="")
            i += 1
            j -= 1
        print(" | ", end="")


if __name__ == "__main__":
    matrix: list[str] = []
    with open("puzzle.txt", "r") as file:
        matrix.extend(line.replace("\n", "") for line in file)
    print(solution(matrix))
