# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        queue = [root]
        last_visited = 1
        i = 0
        reverse = False
        level = []

        while queue and i != last_visited:
            cur = queue[i]
            level.append(cur.val)
            i += 1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if i == last_visited:
                if reverse:
                    level.reverse()
                result.append(level)
                reverse = not reverse
                level = []
                last_visited = len(queue)
        return result