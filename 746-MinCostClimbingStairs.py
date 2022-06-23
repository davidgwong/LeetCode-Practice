""" Done! """

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

"""

from typing import List, Optional

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        P1 = cost[n-2]
        P2 = cost[n-1]

        for i in range(n-2):
            it = cost[n-3-i] + min(P1, P2)
            P2 = P1
            P1 = it
        
        return min(P1,P2)

soln = Solution()

cost = [10,15,20]
print('Answer = 15. Test case: ', end=''), print(soln.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print('Answer = 6. Test case: ', end=''), print(soln.minCostClimbingStairs(cost))