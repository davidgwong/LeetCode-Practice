""" Done! """

""" Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "". """

from typing import List, Optional

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        ans = ""
        it = 0
        
        for ch in strs[0]:
            for ea in strs[1:]:
                if it >= len(ea):
                    return ans
                if ch != ea[it]:
                    return ans
            ans += ch
            it += 1
        
        return ans

soln = Solution()

strs = ["flower","flow","flight"]
print('Answer = "fl". Test case: "', end=''), print(soln.longestCommonPrefix(strs), end=''), print('"')

strs = ["dog","racecar","car"]
print('Answer = "". Test case: "', end=''), print(soln.longestCommonPrefix(strs), end=''), print('"')

strs = ["flower"]
print('Answer = "flower". Test case: "', end=''), print(soln.longestCommonPrefix(strs), end=''), print('"')

strs = ["abcdefghijklmnop","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno","abcdefghijklmno"]
print('Answer = "abcdefghijklmno"". Test case: "', end=''), print(soln.longestCommonPrefix(strs), end=''), print('"')

strs = ["","racecar","race"]
print('Answer = "". Test case: "', end=''), print(soln.longestCommonPrefix(strs), end=''), print('"')