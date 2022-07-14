# Done

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums) - nums[0]
        if l == r:
            return 0

        for i in range(1,len(nums)):
            l += nums[i-1]
            r -= nums[i]
            if l == r:
                return i
        
        return -1

soln = Solution()

nums = [1,7,3,6,5,6]
print("Answer: 3. Output: ", end=""), print(soln.pivotIndex(nums))

nums = [1,2,3]
print("Answer: -1. Output: ", end=""), print(soln.pivotIndex(nums))

nums = [2,1,-1]
print("Answer: 0. Output: ", end=""), print(soln.pivotIndex(nums))