# Done

from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        if len(nums) == threshold:
            return right
        
        while left < right:
            mid = left + (right-left)//2
            sum = 0
            for ea in nums:
                sum += ea//mid
                if ea%mid != 0:
                    sum += 1
            if sum > threshold:
                left = mid+1
            if sum <= threshold:
                right = mid
        return left

soln = Solution()

nums = [1,2,5,9]
threshold = 6
print("Actual: 5. Output: ", end=""), print(soln.smallestDivisor(nums,threshold))

nums = [44,22,33,11,1]
threshold = 5
print("Actual: 44. Output: ", end=""), print(soln.smallestDivisor(nums,threshold))

nums = [1]
threshold = 5
print("Actual: 1. Output: ", end=""), print(soln.smallestDivisor(nums,threshold))

nums = [44,22,33,11,1]
threshold = 10
print("Actual: 15. Output: ", end=""), print(soln.smallestDivisor(nums,threshold))

nums = [2,3,5,7,11]
threshold = 11
print("Actual: 3. Output: ", end=""), print(soln.smallestDivisor(nums,threshold))