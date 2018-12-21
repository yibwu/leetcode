# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        return self.helper(pre, 0, len(pre) - 1, tin, 0, len(tin) - 1)

    def helper(self, pre, low_pre, high_pre, tin, low_tin, high_tin):
        if low_pre <= high_pre:
            target = pre[low_pre]
            i = low_tin
            while i <= high_tin and tin[i] != target:
                i += 1
            root = TreeNode(target)
            root.left = self.helper(pre, low_pre + 1, i - low_tin + low_pre, tin, low_tin, i - 1)
            root.right = self.helper(pre, i - low_tin + low_pre + 1, high_pre, tin, i + 1, high_tin)
            return root
        else:
            return None

    def walk_tree(self, root):
        if root:
            print(root.val)
            self.walk_tree(root.left)
            self.walk_tree(root.right)


if __name__ == '__main__':
    o = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    root = o.reConstructBinaryTree(pre, tin)
    o.walk_tree(root)