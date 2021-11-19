class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count = 0
        result = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             result.append(nums1[i])
        #             nums2.remove(nums2[j])
        # return result

        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result


