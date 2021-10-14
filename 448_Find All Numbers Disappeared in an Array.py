class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # print(n)
        # print(i)
        # print(nums[i])
        # if i == nums[i]:
        result = []
        nums = set(nums)
        # print(nums)
        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)
        return result



