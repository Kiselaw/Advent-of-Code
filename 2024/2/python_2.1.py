def solution(list_of_arrays: list) -> int:
    counter = 0
    for array in list_of_arrays:
        res = all(i > j and 1 <= i - j <= 3 for i, j in zip(array, array[1:])) or all(
            i < j and 1 <= j - i <= 3 for i, j in zip(array, array[1:])
        )
        if res:
            counter += 1
    return counter


if __name__ == "__main__":
    list_of_arrays = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            list_of_arrays.append(list(map(int, line.split())))
    print(solution(list_of_arrays))
