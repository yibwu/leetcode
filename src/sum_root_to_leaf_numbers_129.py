# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left 
        self.right = right 


class Solution:
    def sum_numbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = self.get_ancestor(root)
        return sum

    def get_ancestor(self, root):
        stack = []
        p = root
        last_visited = None
        sum = 0

        while p or len(stack) > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                cur = stack[-1]
                if cur.right and cur.right != last_visited:
                    p = cur.right
                else:
                    if cur.left is None and cur.right is None:
                        t = self.sum_of_path(stack)
                        sum += t
                    last_visited  = stack.pop() 
        return sum 

    def sum_of_path(self, path):
        n = 0
        for p in path:
            n = 10 * n + p.val
        return n


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(5, TreeNode(6, None, None), TreeNode(2, TreeNode(7, None, None), TreeNode(4, None, None))), TreeNode(1, TreeNode(0, None, None), TreeNode(8, None, None))) 
    o = Solution()
    ret = o.sum_numbers(root)
    print(ret)
