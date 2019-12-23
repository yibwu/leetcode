# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = [None]
        return self.helper(prev, root)
    
    def helper(self, prev, root):
        if root:
            ret = self.helper(prev, root.left)
            if ret:
                p = prev[0]
                prev[0] = root
                if not p:
                    return self.helper(prev, root.right)
                else:
                    return p.val < root.val and self.helper(prev, root.right)
            else:
                return False
        else:
            return True
