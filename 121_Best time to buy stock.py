class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #         for i in range(len(prices)-1):
        #             for j in range(i + 1, len(prices)):
        #                 profit = prices[j] - prices[i]
        #                 print(profit)
        #                 if profit > max_profit:
        #                     max_profit = profit

        #             return max_profit

        minimum = max(prices)
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = max(profit, prices[i] - minimum)

        return profit









