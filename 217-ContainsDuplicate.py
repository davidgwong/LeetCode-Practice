# Done

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for n in nums:
            if n in d:
                return True
            else:
                d.add(n)
        return False

soln = Solution()

nums = [1,2,3,1]
print("Answer: True. Output: ", end=''), print(soln.containsDuplicate(nums))

nums = [1,2,3,4]
print("Answer: False. Output: ", end=''), print(soln.containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print("Answer: True. Output: ", end=''), print(soln.containsDuplicate(nums))

nums = [1]
print("Answer: False. Output: ", end=''), print(soln.containsDuplicate(nums))