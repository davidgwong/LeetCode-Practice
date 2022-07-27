# Done

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right,q.right):
            return False
        return True
        
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().isSameTree(p,q))

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(Solution().isSameTree(p,q))