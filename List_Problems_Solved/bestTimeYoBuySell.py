"""
maxProfit - function to return maximu profit (leetcode 121)
@prices: List of prices
Return: 0 if maxProfit < 0 else maxProfit
(using slide window technique)
"""
def maxProfit(prices):
    maxProfit = float("-inf")
    profit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(profit,maxProfit)
        else:
            left = right
        right += 1
    return 0 if maxProfit < 0 else maxProfit
