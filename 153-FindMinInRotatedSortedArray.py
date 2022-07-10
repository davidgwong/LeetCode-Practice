# Done

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        mid = left + (right-left)//2

        while left < right:
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            if nums[mid] <= nums[right] <= nums[left]:
                right = mid
                left += 1
            else:
                left = mid + 1
            mid = left + (right-left)//2
        return nums[left]

soln = Solution()

# right < left < mid
nums = [3,4,5,1,2]
print("Expected: 1. Output: ", end=""), print(soln.findMin(nums))

# mid < right < left
nums = [7,0,1,2,4,5,6]
print("Expected: 0. Output: ", end=""), print(soln.findMin(nums))

# left < mid < right
nums = [11,13,15,17]
print("Expected: 11. Output: ", end=""), print(soln.findMin(nums))

nums = [4,5,6,7,0,1,2]
print("Expected: 0. Output: ", end=""), print(soln.findMin(nums))