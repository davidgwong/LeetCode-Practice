# Done. There are "cheating" ways in Python...

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0,len(s)-1

        while l<r:
            foo, bar = s[l], s[r]
            s[l], s[r] = bar, foo
            l += 1
            r -= 1

s = ["h","e","l","l","o"]
Solution().reverseString(s)
print("Answer: [o,l,l,e,h]. Output: ", end=""), print(s)