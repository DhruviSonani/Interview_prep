def lengthOfLIS(nums):
    # Tc - O(n^log(n))
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
        if dp[left] < nums[i]:
            dp.append(nums[i])
            len_dp += 1
        else:
            dp[left] = nums[i]
    print(dp)
    return len_dp


nums = [4, 10, 4, 3, 8, 9]
print(lengthOfLIS(nums))
