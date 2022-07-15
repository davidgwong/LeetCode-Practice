from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r,ans = [1]*n,[1]*n,[1]*n
        l[1] = nums[0]
        r[n-2] = nums[n-1]
        for i in range(2,len(nums)):
            l[i] = nums[i-1]*l[i-1]
            r[n-i-1] = nums[n-i]*r[n-i]
        for k in range(len(nums)):
            ans[k] = l[k]*r[k]
        return ans

soln = Solution()

nums = [1,2,3,4]
print("Answer: [24,12,8,6]. Output: ", end=""), print(soln.productExceptSelf(nums))