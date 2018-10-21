"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.getMaxDepth(root)

    def getMaxDepth(self, root):
        if root:
            depths = []
            for ch in root.children:
                d = self.getMaxDepth(ch)
                depths.append(d)
            return max(depths) + 1 if depths else 1
        else:
            return 0