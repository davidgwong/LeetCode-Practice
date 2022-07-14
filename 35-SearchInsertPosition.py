# Done

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)
        
        while l<r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        
        return l

soln = Solution()

nums = [1,3,5,6]
target = 5
print("Answer: 2. Output: ", end=""), print(soln.searchInsert(nums,target))

nums = [1,3,5,6]
target = 7
print("Answer: 4. Output: ", end=""), print(soln.searchInsert(nums,target))

nums = [1,3,5,6]
target = 2
print("Answer: 1. Output: ", end=""), print(soln.searchInsert(nums,target))