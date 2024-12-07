def check_is_safe(array):
    return all(i > j and 1 <= i - j <= 3 for i, j in zip(array, array[1:])) or all(
        i < j and 1 <= j - i <= 3 for i, j in zip(array, array[1:])
    )


def solution(list_of_arrays: list) -> int:
    counter = 0
    for array in list_of_arrays:
        check = check_is_safe(array)
        if check:
            counter += 1
        elif not check:
            for i in range(len(array)):
                dempered_array = array[:i] + array[i + 1 :]
                check = check_is_safe(dempered_array)
                if check:
                    counter += 1
                    break
    return counter


if __name__ == "__main__":
    list_of_arrays = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            list_of_arrays.append(list(map(int, line.split())))
    print(solution(list_of_arrays))
