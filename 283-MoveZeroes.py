# Done

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,1

        while r < len(nums):
            if nums[l] == 0:
                while r < len(nums)-1 and nums[r] == 0:
                    r += 1
                nums[l],nums[r] = nums[r], nums[l]
            l += 1
            while r < l:
                r += 1

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print("Answer: [1,3,12,0,0]. Output: ", end=""), print(nums)

nums = [0]
Solution().moveZeroes(nums)
print("Answer: [0]. Output: ", end=""), print(nums)

nums = [0,1]
Solution().moveZeroes(nums)
print("Answer: [1,0]. Output: ", end=""), print(nums)

nums = [1,0]
Solution().moveZeroes(nums)
print("Answer: [1,0]. Output: ", end=""), print(nums)

nums = [0,0]
Solution().moveZeroes(nums)
print("Answer: [0,0]. Output: ", end=""), print(nums)