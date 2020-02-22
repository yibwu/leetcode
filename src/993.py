# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = [root]
        a_dict = dict({root: None})
        last_visited = root
        level = 0
        x_level, x_parent = 0, None
        y_level, y_parent = 0, None
        
        while queue:
            cur = queue.pop(0)
            if cur.val == x:
                x_level = level
                x_parent = a_dict[cur]
            elif cur.val == y:
                y_level = level
                y_parent = a_dict[cur]
            
            if cur.left:
                a_dict[cur.left] = cur
                queue.append(cur.left)
            if cur.right:
                a_dict[cur.right] = cur
                queue.append(cur.right)
            if cur == last_visited:
                level += 1
                if queue:
                    last_visited = queue[-1]
        return True if x_level == y_level and x_parent != y_parent else False
