# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.remove_zero_subtree(root)
        return root

    def remove_zero_subtree(self, root):
        if root is not None:
            if not self.contains_one(root.left):
                root.left = None
            else:
                self.remove_zero_subtree(root.left)
            if not self.contains_one(root.right):
                root.right = None
            else:
                self.remove_zero_subtree(root.right)

    def contains_one(self, root):
        if root is None:
            return False
        else:
            return root.val == 1 \
                   or self.contains_one(root.left) \
                   or self.contains_one(root.right)
