class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        operations_dict = {"--X": -1, "++X": 1, "X--": -1, "X++": 1}
        for i in operations:
            x = x + operations_dict[i]

        return x
