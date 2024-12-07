def solution(array_1: list[int], array_2: list[int]) -> int:
    uniq_nums = set(array_1)
    counter = {}
    for i in uniq_nums:
        if i not in counter:
            counter[i] = 0
        for j in array_2:
            if i == j:
                counter[i] += 1
    return sum([i[0] * i[1] for i in counter.items()])


if __name__ == "__main__":
    array_1 = []
    array_2 = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            a, b = line.split()
            array_1.append(int(a))
            array_2.append(int(b))
    print(solution(array_1, array_2))
