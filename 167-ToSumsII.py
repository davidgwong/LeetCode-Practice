""" Done! """

from typing import List
"""
- There is exactly one solution.
- 1-indexed array of integers that is sorted in an increasing order.
- -1000 <= numbers[i] <= 1000
- -1000 <= target <= 1000
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        rear = len(numbers) - 1

        while(front < len(numbers) and rear > 0):
            if(numbers[front] + numbers[rear] == target):
                return [front+1, rear+1]
            if(numbers[front] + numbers[rear] > target):
                rear -= 1
            if(numbers[front] + numbers[rear] < target):
                front += 1

soln = Solution()

numbers = [2,7,11,15]
target = 9
print('Test case 1 [1,2]: ', end=''), print(soln.twoSum(numbers,target))

numbers = [2,3,4]
target = 6
print('Test case 2 [1,3]: ', end=''), print(soln.twoSum(numbers,target))

numbers = [-1,0]
target = -1
print('Test case 3 [1,2]: ', end=''), print(soln.twoSum(numbers,target))