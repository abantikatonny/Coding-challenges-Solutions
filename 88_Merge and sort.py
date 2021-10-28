class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # result1 = []
        for i in range(n):
            nums1[i + m] = nums2[i]
        print(nums1)

        nums1.sort()




