# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        return self.helper(root)

    def helper(self, root):
        if root:
            left = self.helper(root.left)
            right = self.helper(root.right)
            root.left = right
            root.right = left
            return root
        else:
            return root

    def walk_tree(self, root):
        if root:
            self.walk_tree(root.left)
            self.walk_tree(root.right)
            print(root.val)


if __name__ == '__main__':
    o = Solution()
    root = TreeNode(8, TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, None, None), None), None), None), None)
    ret = o.Mirror(root)
    o.walk_tree(ret)

