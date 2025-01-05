def check(target: int, nums: tuple[int, ...]) -> bool:
    curr_num, r_nums = nums[-1], nums[:-1]
    if len(nums) == 1:
        return target == nums[0]
    n_target, mod = divmod(target, curr_num)
    if mod == 0 and check(n_target, r_nums):
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
