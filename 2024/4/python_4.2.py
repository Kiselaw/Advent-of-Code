def solution(matrix: list[str]) -> int:
    patterns = ["MMASS", "SSAMM", "MSAMS", "SMASM"]
    res = 0
    max_col_len = len(matrix[0])
    max_row_len = len(matrix)
    strings = []
    for i in range(max_row_len - 2):
        for j in range(max_col_len - 2):
            # Extract the 3x3 submatrix and convert it to string without unnecessary chars
            string = "".join([row[j : j + 3] for row in matrix[i : i + 3]])[::2]
            strings.append(string)
    for string in strings:
        if string in patterns:
            res += 1
    return res


if __name__ == "__main__":
    matrix: list[str] = []
    with open("puzzle.txt", "r") as file:
        matrix.extend(line.strip() for line in file)
    print(solution(matrix))
