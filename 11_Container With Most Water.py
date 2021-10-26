class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        #         value = 0

        #         for l in range(len(height)):
        #             for r in range(len(height)):
        #                 area = (l-r) * min(height[l], height[r])
        #                 value = max(value, area)
        #         return value

        res = 0
        l, r = 0, len(height) - 1

        while l < r:

            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res







