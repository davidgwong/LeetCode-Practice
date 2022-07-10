# Done

"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)*len(matrix[0])
        mid = right//2

        m, n = len(matrix), len(matrix[0])

        while mid != left and mid!= right:
            if matrix[mid//n][mid%n] == target:
                return True
            if matrix[mid//n][mid%n] < target:
                left = mid
            else:
                right = mid
            mid = (left + right)//2

        if matrix[mid//n][mid%n] == target:
            return True
        return False

soln = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print("Actual = True. Output = ", end=""), print(soln.searchMatrix(matrix,target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print("Actual = False. Output = ", end=""), print(soln.searchMatrix(matrix,target))

matrix = [[1,3]]
target = 2
print("Actual = False. Output = ", end=""), print(soln.searchMatrix(matrix,target))