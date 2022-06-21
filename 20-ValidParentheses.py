""" Done! """

class Solution:
    def isValid(self, s: str) -> bool:
        if ((len(s) % 2) != 0):
            return False

        myStack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                myStack.append(ch)
            if ch == ')' or ch == ']' or ch == '}':
                if len(myStack) == 0:
                    return False
                if ch == ')':
                    if myStack.pop() != '(':
                        return False
                if ch == ']':
                    if myStack.pop() != '[':
                        return False
                if ch == '}':
                    if myStack.pop() != '{':
                        return 

        if len(myStack) != 0:
            return False
        return True

ans = Solution()

mySolution = ans.isValid("()")
print('Test case 1 (True): ', end=''), print(mySolution)

mySolution = ans.isValid("()[]{}")
print('Test case 2 (True): ', end=''), print(mySolution)

mySolution = ans.isValid("(]")
print('Test case 3 (False): ', end=''), print(mySolution)

mySolution = ans.isValid("[[[((()))]]]")
print('Test case 4 (True): ', end=''), print(mySolution)

mySolution = ans.isValid("((")
print('Test case 5 (False): ', end=''), print(mySolution)

mySolution = ans.isValid("){")
print('Test case 6 (False): ', end=''), print(mySolution)