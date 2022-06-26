"""

---Done!---

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
    1 <= n <= 45

"""

from typing import List, Optional

class Solution:
    def climbStairs(self, n: int) -> int:
        l,r = 1,1

        if(n == 1):
            return l
        
        for i in range(n-1):
            tmp = l
            l += r
            r = tmp
        return l

soln = Solution()

n = 1
print("Answer: 1. Output: ", end=''), print(soln.climbStairs(n))

n = 2
print("Answer: 2. Output: ", end=''), print(soln.climbStairs(n))

n = 3
print("Answer: 3. Output: ", end=''), print(soln.climbStairs(n))

n = 4
print("Answer: 5. Output: ", end=''), print(soln.climbStairs(n))