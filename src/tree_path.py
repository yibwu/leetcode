# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        stack = []
        result = []
        p = root
        last_visited = None

        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                cur = stack[-1]
                if cur.right and cur.right != last_visited:
                    p = cur.right
                else:
                    cur = stack.pop()
                    last_visited = cur
                    if not cur.left and not cur.right:
                        arr = list(map(lambda x: x.val, stack))
                        s = sum(arr)
                        if s + cur.val == expectNumber:
                            result.append(arr + [cur.val])
        result.sort(key=len, reverse=True)
        return result


if __name__ == '__main__':
    o = Solution()
    root = TreeNode(10, TreeNode(5, TreeNode(4, None, None), TreeNode(7, None, None)), TreeNode(12, None, None))
    ret = o.FindPath(root, 22)
    print(ret)