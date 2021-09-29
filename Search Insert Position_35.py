def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target or nums[i] > target:
            return (i)
        elif nums[i] < target:
            pass
    print(len(nums))



searchInsert([1,3,5,6], 5)