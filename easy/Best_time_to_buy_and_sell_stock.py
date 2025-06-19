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
        #sets intial first buy
        max_prices = 0
        temp_buy = prices[0]
        #checks each day when to sell and buy setting the new minimums and profits each day 
        # greedy approach checking each value O(n)
        for buy in range(len(prices)):
            if prices[buy] < temp_buy:
                temp_buy = prices[buy]
            else:
                profits = prices[buy] - temp_buy
                max_prices = profits
        return max_prices