# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        tmp = root
        while tmp and tmp.val != val:
            if tmp.val > val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return tmp