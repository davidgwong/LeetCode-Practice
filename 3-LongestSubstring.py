""" Done! """

"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        max = 0
        mySet = set()
        myList = list()

        for ea in s:
            if ea in mySet:
                front = myList.pop(0)
                mySet.remove(front)

                while(front != ea):
                    front = myList.pop(0)
                    mySet.remove(front)

                mySet.add(ea)
                myList.append(ea)
                curr = len(myList)
                
            else:
                mySet.add(ea)
                myList.append(ea)
                curr += 1
                if curr > max:
                    max = curr
        
        return max

soln = Solution()

s = "abcabcbb"
print('Answer = 3. Test case: ', end=''), print(soln.lengthOfLongestSubstring(s))

s = "bbbbb"
print('Answer = 1. Test case: ', end=''), print(soln.lengthOfLongestSubstring(s))

s = "pwwkew"
print('Answer = 3. Test case: ', end=''), print(soln.lengthOfLongestSubstring(s))

s = "aab"
print('Answer = 2. Test case: ', end=''), print(soln.lengthOfLongestSubstring(s))