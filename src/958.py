# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = [root]
        while queue:
            cur = queue.pop(0)
            
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
            elif queue and queue.count(None) != len(queue):
                return False
            else:
                pass
        return True
