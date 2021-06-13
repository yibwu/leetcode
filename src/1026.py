# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        queue = [root]
        res = 0
        while queue:
            cur = queue.pop()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            arr = [1e5+1, -1]
            self.getMaxAndMinFromSubTree(cur, arr)
            t = max(abs(cur.val-arr[0]), abs(cur.val-arr[1]))
            if t > res:
                res = t
        return res
    
    def getMaxAndMinFromSubTree(self, root, arr):
        if root:
            if root.val < arr[0]:
                arr[0] = root.val
            if root.val > arr[1]:
                arr[1] = root.val
            self.getMaxAndMinFromSubTree(root.left, arr)
            self.getMaxAndMinFromSubTree(root.right, arr)

