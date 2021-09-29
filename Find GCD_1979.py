def gcd(nums):
    max_num = nums[0]
    min_num = nums[0]
    for i in nums:
        min_num = min(i, min_num)
        max_num = max(i, max_num)
    print(min_num, max_num)

    def GCDfind(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return GCDfind(min_num, max_num)
#
print(gcd([3,3]))
    