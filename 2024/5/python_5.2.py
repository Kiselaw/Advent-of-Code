from typing import Set, Tuple


def sort_rules(rules: list[Tuple]) -> dict[str, Set]:
    sorted_rules: dict[str, Set] = {num: set() for num, rule in rules}
    for _, rule in rules:
        if rule not in sorted_rules:
            sorted_rules[rule] = set()
    for rule in rules:
        sorted_rules[rule[0]].add(rule[1])
    return sorted_rules


def get_invalid_updates(
    sorted_rules: dict[str, Set], updates: list[list[str]]
) -> list[list[str]]:
    invalid_updates = []
    for update in updates:
        for i in range(len(update) - 1):
            if not set(update[i + 1 :]).issubset(sorted_rules[update[i]]):
                invalid_updates.append(update)
                break
    return invalid_updates


def correct_invalid_updates(
    sorted_rules: dict[str, Set], invalid_updates: list[list[str]]
) -> list[list[str]]:
    for update in invalid_updates:
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[i] in sorted_rules[update[j]]:
                    update[i], update[j] = update[j], update[i]
    return invalid_updates


def solution(rules: list[Tuple], updates: list[list[str]]) -> int:
    sorted_rules = sort_rules(rules)
    invalid_updates = get_invalid_updates(sorted_rules, updates)
    corrected_updates = correct_invalid_updates(sorted_rules, invalid_updates)
    counter = 0
    for update in corrected_updates:
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
