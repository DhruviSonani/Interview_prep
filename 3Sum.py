class Solution:
    def twoSumSorted(self, next_index, end_index, arr, target, res):
        a1 = arr[next_index - 1]
        while next_index < end_index:
            # if target exceeds move starting pointer
            if arr[end_index] + arr[next_index] > target:
                end_index -= 1
            # if target is less than target, move end pointer
            elif arr[end_index] + arr[next_index] < target:
                next_index += 1
            else:
                # if addition is same as target
                temp = []
                temp.append(a1)
                temp.append(arr[next_index])
                temp.append(arr[end_index])

                # append in result
                res.append(temp)

                # in inner loop of next and end pointer, check if value is same
                while next_index < end_index and arr[next_index] == arr[next_index+1]:
                    next_index += 1
                while next_index < end_index and arr[end_index] == arr[end_index-1]:
                    end_index -= 1

                next_index += 1
                end_index -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # Check if current and next value are not same
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumSorted(i+1, len(nums)-1, nums, 0-nums[i], res)
        return res
