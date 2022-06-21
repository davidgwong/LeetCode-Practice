""" Done! """

from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in an increasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in an increasing order.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        it = m + n

        while( (it > 0)):
            print('it: ', end=''), print(it, end=''), print(', m: ', end=''), print(m, end=''), print(', n: ', end=''), print(n, end=''), print(', nums1: ', end=''), print(nums1)
            if(n == 0):
                nums1[it-1] = nums1[m-1]
                m -=1
            elif(m == 0):
                nums1[it-1] = nums2[n-1]
                n -= 1
            elif(nums1[m-1] > nums2[n-1]):
                nums1[it-1] = nums1[m-1]
                m -= 1
            else:
                nums1[it-1] = nums2[n-1]
                n -= 1
            it -= 1

ans = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

ans.merge(nums1,m,nums2,n)
print('Test case 1: ', end=''), print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0

ans.merge(nums1,m,nums2,n)
print('Test case 2: ', end=''), print(nums1)

nums1 = [0,0]
m = 0
nums2 = [1,2]
n = 2

ans.merge(nums1,m,nums2,n)
print('Test case 3: ', end=''), print(nums1)