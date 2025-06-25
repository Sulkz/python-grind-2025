"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


"Brute Force but doesnt work as well O(n^2)"
class Solution(object):
    def maxProfit(self, prices):
        max_profits = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1,len(prices)):
                profit = prices[sell] - prices[buy]
                max_profits = profit
        return max_profits
        

"Greedy optimised O(n)"
class Solution(object):
    def maxProfit(self, prices):
        max_points = 0
        temp_buy = prices[0]
        for x in (len(prices)):
           if prices[x] < temp_buy:
               temp_buy = prices[x]
           else:
               profits = prices[x] - temp_buy
               max_points = profits
        return max_points