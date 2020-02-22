# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return
        
        self.a_set = set([0])
        queue = [root]
        a_dict = dict({root: 0})
        
        while queue:
            cur = queue.pop(0)
            x = a_dict[cur]
            cur.val = x
            if cur.left:
                left_val = 2 * x + 1
                a_dict[cur.left] = left_val
                self.a_set.add(left_val)
                queue.append(cur.left)
            if cur.right:
                right_val = 2 * x + 2
                a_dict[cur.right] = right_val
                self.a_set.add(right_val)
                queue.append(cur.right)

    def find(self, target: int) -> bool:
        return target in self.a_set
