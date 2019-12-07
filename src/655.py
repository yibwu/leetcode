# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        h = self.height(root)
        width = 2 ** h - 1
        res = [[''] * width for _ in range(h)]
        
        h -= 2
        node_position = dict()
        node_position[root] = (0, width // 2)
        res[0][width // 2] = str(root.val)
        last_visited = root
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                px, py = node_position[cur]
                x = px + 1
                y = py - 2 ** h
                res[x][y] = str(cur.left.val)
                node_position[cur.left] = (x, y)
            if cur.right:
                queue.append(cur.right)
                px, py = node_position[cur]
                x = px + 1
                y = py + 2 ** h
                res[x][y] = str(cur.right.val)
                node_position[cur.right] = (x, y)
            if last_visited == cur and queue:
                last_visited = queue[-1]
                h -= 1
        return res
            
    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
