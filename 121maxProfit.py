class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        if len(prices):
            minprice=prices[0]
            for curprice in prices:
                minprice=min(minprice, curprice)
                maxprofit=max(maxprofit,curprice-minprice)
        return maxprofit
