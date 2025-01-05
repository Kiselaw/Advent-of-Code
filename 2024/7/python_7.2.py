def check_concat(curr_num, target) -> bool:
    while curr_num != 0:
        if curr_num % 10 == target % 10:
            curr_num //= 10
            target //= 10
            continue
        else:
            return False
    return True


def update_target(curr_num, target) -> int:
    curr_num = str(curr_num)
    for i in range(len(curr_num)):
        target //= 10
    return target


def check(target: int, nums: tuple[int, ...]) -> bool:
    curr_num, r_nums = nums[-1], nums[:-1]
    if len(nums) == 1:
        return target == nums[0]
    n_target, mod = divmod(target, curr_num)
    if mod == 0 and check(n_target, r_nums):
        return True
    if check_concat(curr_num, target) and check(
        update_target(curr_num, target), r_nums
    ):
        return True
    return check(target - curr_num, r_nums)


def solution(target: int, nums: tuple[int, ...]) -> int:
    if check(target, nums):
        return target
    return 0


if __name__ == "__main__":
    res: list[int] = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            target, nums = line.split(":")
            int_target: int = int(target)
            tuple_nums: tuple[int, ...] = tuple(map(int, nums.strip().split(" ")))
            res.append(solution(int_target, tuple_nums))
    print(sum(res))
