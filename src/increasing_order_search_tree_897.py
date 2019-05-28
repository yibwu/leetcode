# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def increasing_BST(self, root):
        if not root:
            return None
        
        res = []
        self.walk_tree(root, res)
        for node in res:
            node.left = None
            node.right = None
            
        tmp, root = res[0], res[0]
        for node in res[1:]:
            tmp.right = node
            tmp = node
        return root

    def walk_tree(self, root, res):
        if root:
            self.walk_tree(root.left, res)
            res.append(root)
            self.walk_tree(root.right, res)
