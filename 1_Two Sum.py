# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i != j and nums[i] + nums[j] == target:
    #                 return [i, j]


nums = [2, 7, 11, 15]
target = 9
hashmap = {}
for i in range(len(nums)):
    hashmap[nums(i)] = i
print(hashmap.items())



