from bisect import bisect_left, bisect_right


def lengthOfLIS(nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        print(dp)
        return max_len
        

nums = [4, 10, 4, 3, 8, 9]
print(lengthOfLIS(nums))
