class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        for i in range(len(prices) - 1):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                maxProfit = max((prices[r] - prices[l]), maxProfit)
                r += 1

        return maxProfit
        
