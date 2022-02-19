import math


def secondSmallest(nums):
    if len(nums) < 2:
        return False

    first, second = math.inf, math.inf
    for i in range(len(nums)):
        if nums[i] < first:
            second, first  = first, nums[i]
        elif nums[i] < second  and nums[i] != first:
            second = nums[i]
    return second



nums = [12, 13, 1, 10,10,15, 34, 1,1]
print(secondSmallest(nums))
