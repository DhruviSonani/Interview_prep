def maxSubArray(nums):

    # currSum = nums[0]
    maxSum = nums[0]

    for i in range(len(nums)):
        currSum = nums[i]
        if (currSum > maxSum):
            maxSum = currSum

        for j in range(i+1, len(nums)):
            currSum += nums[j]
            if (currSum > maxSum):
                maxSum = currSum

    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
