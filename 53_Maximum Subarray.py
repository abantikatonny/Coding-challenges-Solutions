class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        first_array = max_array = nums[0]
        # print(result)
        # for i in range(len(nums)):
        for num in nums[1:]:
            # print(num)
            # print(nums[i])
            first_array = max(num, first_array + num)
            max_array = max(max_array, first_array)
            # print(first_array)
            # result = max(sum, result)
        # print(result)
        return max_array


