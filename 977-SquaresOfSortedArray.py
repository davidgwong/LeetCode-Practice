# Done. But a better way is to start at the extremes, instead of closest to num[i] = 0.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = self.findClosesZeroValueIndex(nums)
        left, right = start-1, start+1
        ans = [nums[start]*nums[start]]

        while left >= 0 and right <= len(nums)-1:
            if abs(nums[left]) < nums[right]:
                ans.append(nums[left]*nums[left])
                left -= 1
            else:
                ans.append(nums[right]*nums[right])
                right += 1

        while left >= 0:
            ans.append(nums[left]*nums[left])
            left -= 1
        
        while right <= len(nums)-1:
            ans.append(nums[right]*nums[right])
            right += 1
        
        return ans

    
    def findClosesZeroValueIndex(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l < r - 1:
            mid = l + (r-l)//2
            if nums[mid] == 0:
                return mid
            if nums[mid] > 0:
                r = mid
            else:
                l = mid
        if abs(nums[l]) < abs(nums[r]):
            return l
        return r

soln = Solution()

nums = [-4,-1,0,3,10]
print("Answer: [0,1,9,16,100]. Output: ", end=""), print(soln.sortedSquares(nums))

nums = [-1,2,2]
print("Answer: [1,4,4]. Output: ", end=""), print(soln.sortedSquares(nums))

nums = [-2,-1,3]
print("Answer: [1,4,9]. Output: ", end=""), print(soln.sortedSquares(nums))