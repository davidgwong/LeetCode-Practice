# Done

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepthHelper(root.left,1),self.maxDepthHelper(root.right,1))

    def maxDepthHelper(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return max(self.maxDepthHelper(root.left, depth+1), self.maxDepthHelper(root.right,depth+1))


soln = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Answer: 3. Output: ", end=""),print(soln.maxDepth(root))