class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            cur = self.stack.pop()
            p = cur.right
            while p:
                self.stack.append(p)
                p = p.left
            return cur.val


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, None, None))
    bst_iter = BSTIterator(root)

    while bst_iter.hasNext():
        print(bst_iter.next())