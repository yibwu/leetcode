# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        pre, p = root, root

        while p:
            if val < p.val:
                pre = p
                p = p.left
            else:
                pre = p
                p = p.right
        if pre:
            if val < pre.val:
                pre.left = TreeNode(val)
            else:
                pre.right = TreeNode(val)
        else:
            root = TreeNode(val)
        return root