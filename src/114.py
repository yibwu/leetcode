# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        p = root
        pre = TreeNode()
        t = pre
        while p or stack:
            if p:
                stack.append(p)
                pre.left = p
                pre = p
                p = p.left
            else:
                x = stack.pop()
                if x.right:
                    p = x.right
        
        p = t.left
        while p:
            p.right = p.left
            p.left = None
            p = p.right
        return t.left
        
