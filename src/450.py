# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def findLeftMost(self, parent, root):
        while root and root.left:
            parent = root
            root = root.left
        fromLeft = parent.left == root
        if fromLeft:
            parent.left = root.right
        else:
            parent.right = root.right
        return root
    
    def findRightMost(self, parent, root):
        while root and root.right:
            parent = root
            root = root.right
        fromLeft = parent.left == root
        if fromLeft:
            parent.left = root.left
        else:
            parent.right = root.left
        return root
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # make sure deleted node has a parent, so we can simplify code when trying to delete root node
        tmp = TreeNode(-999999, root, None) 
        parent, cur = tmp, root
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        # key not found
        if not cur:
            return root
            
        fromLeft = parent.left == cur
        if cur.left:
            x = self.findRightMost(cur, cur.left)
            x.left = cur.left
            x.right = cur.right if cur.right != x else x.right
        elif cur.right:
            x = self.findLeftMost(cur, cur.right)
            x.left = cur.left if cur.left != x else x.left
            x.right = cur.right
        else:
            x = None

        if fromLeft:
            parent.left = x
        else:
            parent.right = x
        return tmp.left
        
