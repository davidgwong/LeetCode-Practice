# Done

""" 
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
 """

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = left + (right-left)//2

        while left < right:
            if nums[mid] == target:
                return mid

            if nums[left] < nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                elif nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    return -1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            mid = left + (right-left)//2
        
        if nums[left] == target:
            return left
        return -1

soln = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
print("Actual: 4. Output: ", end=""), print(soln.search(nums,target))

nums = [4,5,6,7,0,1,2]
target = 3
print("Actual: -1. Output: ", end=""), print(soln.search(nums,target))

nums = [1]
target = 0
print("Actual: -1. Output: ", end=""), print(soln.search(nums,target))

nums = [1]
target = 1
print("Actual: 0. Output: ", end=""), print(soln.search(nums,target))

nums = [2,1]
target = 1
print("Actual: 1. Output: ", end=""), print(soln.search(nums,target))

nums = [5,1,3]
target = 5
print("Actual: 0. Output: ", end=""), print(soln.search(nums,target))

nums = [4,5,6,7,8,1,2,3]
target = 8
print("Actual: 4. Output: ", end=""), print(soln.search(nums,target))