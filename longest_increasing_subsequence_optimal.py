def lengthOfLIS(nums):
    # Tc - O(n^log(n))
    # we will find very next elemetn of current element to add in list
    if not nums:
        return 0
    dp = [nums[0]]
    len_dp = 1
    for i in range(1, len(nums)):
        left, right = 0, len(dp) - 1
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < nums[i]:
                left = mid + 1
            else:
                right = mid
        print(left, right, dp)
        if dp[left] < nums[i]:
            dp.append(nums[i])
            len_dp += 1
        else:
            dp[left] = nums[i]
    print(dp)
    return len_dp


#     0 0 [10]
# 0 0 [9]
# 0 0 [2]
# 1 1 [2, 5]
# 1 1 [2, 3]
# 2 2 [2, 3, 7]
# 3 3 [2, 3, 7, 101]
# [2, 3, 7, 18]
# 4


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
