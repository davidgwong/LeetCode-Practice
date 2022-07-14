# Done

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

soln = Solution()

nums = [1,2,3,4]
print("Answer: [1,3,6,10]. Output: ", end=""), print(soln.runningSum(nums))

nums = [1,1,1,1,1]
print("Answer: [1,2,3,4,5]. Output: ", end=""), print(soln.runningSum(nums))

nums = [3,1,2,10,1]
print("Answer: [3,4,6,16,17]. Output: ", end=""), print(soln.runningSum(nums))