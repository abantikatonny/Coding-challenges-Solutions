class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #         result = []
        #         for i in nums:
        #             if i not in result:
        #                 result.append(i)
        #             else:
        #                 result.remove(i)

        #         return result.pop()

        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

        # print(hash_table)

