class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for i in reversed(nums):
        # print(i)
        # print(nums[3]
        length = len(nums)
        k = k % length

        firstPart = nums[length - k:]
        secondPart = nums[:length - k]

        nums[:] = firstPart + secondPart

        return nums

