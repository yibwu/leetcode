# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        acc = [0]
        self.helper(root, acc)
        return root
        
    def helper(self, root, acc):
        if root:
            self.helper(root.right, acc)
            acc[0] += root.val
            root.val = acc[0]
            self.helper(root.left, acc)

