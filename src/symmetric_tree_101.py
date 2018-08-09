# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_symmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            root.right = self.swap_tree(root.right)
            return self.is_same_tree(root.left, root.right)
        else:
            return True

    def swap_tree(self, root):
        if root is not None:
            left = self.swap_tree(root.left)
            right = self.swap_tree(root.right)
            root.left = right
            root.right = left
            return root
        else:
            return None

    def is_same_tree(self, root1, root2):
        if root1 is None:
            if root2 is None:
                return True
            else:
                return False
        else:
            if root2 is None:
                return False
            else:
                return root1.val == root2.val and \
                       self.is_same_tree(root1.left, root2.left) and \
                       self.is_same_tree(root1.right, root2.right)
