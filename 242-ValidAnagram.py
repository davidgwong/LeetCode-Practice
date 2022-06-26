"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from operator import truediv
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        return s==t

soln = Solution()

s = "anagram"
t = "nagaram"
print('Answer: True. Output: ', end=''), print(soln.isAnagram(s,t))

s = "rat"
t = "car"
print('Answer: False. Output: ', end=''), print(soln.isAnagram(s,t))

s = "a"
t = "ab"
print('Answer: False. Output: ', end=''), print(soln.isAnagram(s,t))