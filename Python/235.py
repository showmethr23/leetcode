# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#       self.val = val
#       self.left = None
#       self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Solution 1
        # Recursion

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and roo.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
