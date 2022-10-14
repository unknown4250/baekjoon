def solution(nums):
    cnt = len(nums) // 2
    type_nums = len(set(nums))

    return type_nums if type_nums < cnt else cnt