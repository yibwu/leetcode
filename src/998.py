# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        pre, p = None, root
        while p and p.val > val:
            pre = p
            p = p.right
            
        new_node = TreeNode(val, None, None)
        if not pre:
            new_node.left = root
            return new_node
        
        new_node.left = pre.right
        pre.right = new_node
        return root
        
