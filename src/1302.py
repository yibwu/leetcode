# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [root]
        last_visited = root
        res = 0
        while queue:
            cur = queue.pop(0)
            res += cur.val
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if cur == last_visited:
                if queue:
                    res = 0
                    last_visited = queue[-1]
                else:
                    return res
