class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        value = set(nums)

        print(value)
        print(len(value))

        if len(value) == len(nums):
            return False
        else:
            return True

#         for i in nums:
#             for j in range(1, i):
#                 # print(nums[i])
#                 # print(nums[j])
#                 if nums[i] == nums[j]:
#                     return True
#                 else:
#                     return False

