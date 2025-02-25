#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Approach 1:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        profit = 0
        lowest = prices[0]
        
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > profit:
                profit = price - lowest

        return profit
    
prices = [7,1,5,3,6,4]
x= Solution()
x.maxProfit(prices)  