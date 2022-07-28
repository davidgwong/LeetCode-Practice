# Done

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        children = deque()

        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)

        output = [[root.val]]

        if len(children) == 0:
            return output
        
        while len(children) != 0:
            numOfCurrentLevelChildren = len(children)
            vals = []
            for ea in range(numOfCurrentLevelChildren):
                currNode = children.popleft()
                vals.append(currNode.val)
                if currNode.left:
                    children.append(currNode.left)
                if currNode.right:
                    children.append(currNode.right)
            output.append(vals)
                
        return output
    

        
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().levelOrder(root))