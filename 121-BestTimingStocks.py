"""
---Done---

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,m = prices[0], prices[0]
        profit = 0

        for i in prices:
            if i < l:
                l = i
                m = i
            if m < i:
                m = i
                if m-l > profit:
                    profit = m-l

        return profit

soln = Solution()

prices = [7,1,5,3,6,4]
print('Answer = 5. Output = ', end=''), print(soln.maxProfit(prices))

prices = [7,6,4,3,1]
print('Answer = 0. Output = ', end=''), print(soln.maxProfit(prices))

prices = [7]
print('Answer = 0. Output = ', end=''), print(soln.maxProfit(prices))

prices = [2,4,1]
print('Answer = 2. Output = ', end=''), print(soln.maxProfit(prices))