"""
--Done--

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l,r = 0, len(s)-1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        

soln = Solution()
print('Answer = True. Output: ', end=''), print(soln.isPalindrome(""))
print('Answer = True. Output: ', end=''), print(soln.isPalindrome("aba"))
print('Answer = True. Output: ', end=''), print(soln.isPalindrome("abba"))
print('Answer = False. Output: ', end=''), print(soln.isPalindrome("abbac"))
print('Answer = True. Output: ', end=''), print(soln.isPalindrome("A man, a plan, a canal: Panama"))
print('Answer = False. Output: ', end=''), print(soln.isPalindrome("raceacar"))
print('Answer = True. Output: ', end=''), print(soln.isPalindrome(" "))