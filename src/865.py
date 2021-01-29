# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        queue = [root]
        last_level = [root]
        last_visited = root
        child_parent = dict()
        
        while queue:
            cur = queue.pop(0)
            last_level.append(cur)
            if cur.left:
                child_parent[cur.left] = cur
                queue.append(cur.left)
            if cur.right:
                child_parent[cur.right] = cur
                queue.append(cur.right)
            if cur == last_visited and queue:
                last_visited = queue[-1]
                last_level = []
                    
        a_set = set(last_level)
        while len(a_set) != 1:
            t = set()
            for item in a_set:
                t.add(child_parent[item])
            a_set = t
        return list(a_set)[0]
    
