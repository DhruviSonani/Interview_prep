from itertools import islice


def twoSum(nums, target):

    def nth_index(iterable, value, n):
        matches = (idx for idx, val in enumerate(iterable) if val == value)
        return next(islice(matches, n-1, n), None)

    i = 0

    j = len(nums) - 1
    temp = nums.copy()
    temp.sort()
    while (i < j):
        sum = temp[i] + temp[j]

        if (sum == target):
            if (temp[i] != temp[j]):
                return (nums.index(temp[i]), nums.index(temp[j]))

            return (nums.index(temp[i]), nth_index(nums, temp[j], 2))
        elif (sum < target):
            i += 1
        else:
            j -= 1


nums = [0, 4, 3, 0]
target = 0
print(twoSum(nums, target))
