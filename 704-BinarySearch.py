"""
Done.

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)
        middle = end//2
        start = 0
        
        while(middle != start and middle != end):
            if(nums[middle] == target):
                return middle
            if(nums[middle] < target):
                start = middle
            if(nums[middle] > target):
                end = middle
            middle = (start+end)//2
        
        if(nums[middle] == target):
            return middle
        else:
            return -1

soln = Solution()

nums = [-1,0,3,5,9,12]
target = 9
print("Answer = 4. Test case = ", end=''), print(soln.search(nums,target))

nums = [-1,0,3,5,9,12]
target = 2
print("Answer = -1. Test case = ", end=''), print(soln.search(nums,target))

nums = [5]
target = 5
print("Answer = 0. Test case = ", end=''), print(soln.search(nums,target))

nums = [2,5]
target = 2
print("Answer = 0. Test case = ", end=''), print(soln.search(nums,target))