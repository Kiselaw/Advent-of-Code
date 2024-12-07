def solution(array_1: list[int], array_2: list[int]) -> int:
    array_1.sort()
    array_2.sort()
    return sum([abs(array_1[i] - array_2[i]) for i in range(len(array_1))])


if __name__ == "__main__":
    array_1 = []
    array_2 = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            a, b = line.split()
            array_1.append(int(a))
            array_2.append(int(b))
    print(solution(array_1, array_2))
