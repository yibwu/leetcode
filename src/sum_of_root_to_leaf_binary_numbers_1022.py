# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def sum_root_to_leaf(self, root):
        paths = self.get_root_to_leaf_paths(root)
        nums = list(map(lambda x: self.path_to_number(x), paths))
        return sum(nums)
        
    # eg: [1, 0, 0] => 4
    def path_to_number(self, nums):
        nums = list(map(str, nums))
        s = ''.join(nums)
        return int(s, 2)
        
    def get_root_to_leaf_paths(self, root):
        p = root
        last_visited = None
        res = []
        stack = []
        
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                cur = stack[-1]
                if cur.right and cur.right != last_visited:
                    p = cur.right
                else:
                    if not cur.left and not cur.right: 
                        nums = list(map(lambda x: x.val, stack))
                        res.append(nums)
                    last_visited = stack.pop(-1)
        return res
