class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        # print(len(nums))
        n = 2 * len(nums) - 1
        i = 0
        while i <= n:
            # print(nums[i % len(nums)])
            result.append(nums[i % len(nums)])
            i += 1
        return result


