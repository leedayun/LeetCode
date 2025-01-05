class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        tot_profit = 0
        min_price = prices[0]
        [7,3,5,2,6,4]
        for price in prices:
            if price < min_price:
                min_price = price
                profit = 0
            elif price - min_price > profit:
                tot_profit -= profit
                profit = price - min_price
                tot_profit += profit
            else:
                min_price = price
                profit = 0
        return tot_profit
