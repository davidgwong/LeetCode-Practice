# Done

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        # Base case: O(n)
        if h == len(piles):
            return right
        
        # O(n*log(max(piles)))
        while left < right:
            mid = left + (right-left)//2
            t = 0
            for ea in piles:
                t += ea//mid
                if ea%mid != 0:
                    t += 1
            if t > h:
                left = mid + 1
            if t <= h:
                right = mid
        return left

soln = Solution()

piles = [3,6,7,11]
h = 8
print("Expected: 4. Output: ", end=""), print(soln.minEatingSpeed(piles,h))

piles = [30,11,23,4,20]
h = 5
print("Expected: 30. Output: ", end=""), print(soln.minEatingSpeed(piles,h))

piles = [30,11,23,4,20]
h = 6
print("Expected: 23. Output: ", end=""), print(soln.minEatingSpeed(piles,h))

piles = [30,11,23,4,20]
h = 45
print("Expected: 2. Output: ", end=""), print(soln.minEatingSpeed(piles,h))

piles = [30,11,23,4,20]
h = 88
print("Expected: 1. Output: ", end=""), print(soln.minEatingSpeed(piles,h))