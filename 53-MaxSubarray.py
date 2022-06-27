"""
---Done---

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maximum = nums[-1]
        current = nums[-1]

        for i in range(2,len(nums)+1):
            current = max(current + nums[0-i],nums[0-i])
            maximum = max(maximum,current)
        
        return maximum

soln = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(soln.maxSubArray(nums))

nums = [5,4,-1,7,8]
print(soln.maxSubArray(nums))
