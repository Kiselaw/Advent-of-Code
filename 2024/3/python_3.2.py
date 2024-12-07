import re


def solution(lines) -> int:
    updated_lines = lines.replace("\n", "")
    updated_lines = re.sub(r"don't\(\)(.*?)do\(\)", "", updated_lines)
    counter = 0
    valid_values = re.findall(r"mul\(\d{1,3},\d{1,3}\)", updated_lines)
    for values in valid_values:
        num_1, num_2 = re.findall(r"\d+", values)
        counter += int(num_1) * int(num_2)
    return counter


if __name__ == "__main__":
    with open("puzzle.txt", "r") as file:
        lines = "".join(line for line in file)
    print(solution(lines))
