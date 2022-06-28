# Done
"""
Given the root of a binary tree, invert the tree, and return its root.
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        l,r = root.left, root.right

        root.left = self.invertTree(r)
        root.right = self.invertTree(l)

        return root

def printLevelOrder(root: Optional[TreeNode]):
    if not root:
        return
 
    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)
 
    # loop till queue is empty
    while queue:
 
        # process each node in the queue and enqueue their
        # non-empty left and right child
        curr = queue.popleft()
 
        print(curr.val, end=' ')
 
        if curr.left:
            queue.append(curr.left)
 
        if curr.right:
            queue.append(curr.right)

soln = Solution()

root = TreeNode(4, 
                TreeNode(2,
                        TreeNode(1), TreeNode(3)),
                TreeNode(7,
                        TreeNode(6), TreeNode(9)))
printLevelOrder(root)
print('')
printLevelOrder(soln.invertTree(root))