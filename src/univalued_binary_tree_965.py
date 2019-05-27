# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def is_unival_tree(self, root):
        if not root:
            return True

        last_visited = None
        queue = [root]

        while queue:
            cur = queue.pop(0)
            if last_visited is not None and last_visited.val != cur.val:
                return False
            last_visited = cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return True


if __name__ == '__main__':
    obj = Solution()
    root1 = TreeNode(1,
                TreeNode(1, TreeNode(1, None, None), TreeNode(1, None, None)),
                TreeNode(1, None, TreeNode(1, None, None)))
    root2 = TreeNode(2,
                TreeNode(2, TreeNode(5, None, None), TreeNode(2, None, None)),
                TreeNode(2, None, None))
    print(obj.is_unival_tree(root1))
    print(obj.is_unival_tree(root2))
