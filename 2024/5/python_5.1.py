def sort_rules(rules: list[tuple[str, str]]) -> dict[str, set]:
    sorted_rules: dict[str, set] = {num: set() for num, rule in rules}
    for rule in rules:
        sorted_rules[rule[0]].add(rule[1])
    return sorted_rules


def solution(rules: list[tuple], updates: list[list[str]]) -> int:
    sorted_rules = sort_rules(rules)
    valid = True
    counter = 0
    for update in updates:
        for i in range(len(update) - 1):
            if update[i] in sorted_rules:
                if set(update[i + 1 :]).issubset(sorted_rules[update[i]]):
                    valid = True
                    continue
                else:
                    valid = False
                    break
            continue
        if not valid:
            continue
        else:
            counter += int(update[len(update) // 2])
    return counter


if __name__ == "__main__":
    rules = []
    updates = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            if "|" in line:
                rules.append(tuple(line.strip().split("|")))
            elif not line.strip():
                continue
            else:
                updates.append(line.strip().split(","))
    print(solution(rules, updates))
