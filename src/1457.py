# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def isPseudoPalindromic(self, nums):
        acc = 0
        for n in nums:
            if n & 1 == 1:
                acc += 1
        return acc < 2
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        stack = []
        p = root
        lastVisited = None
        res = 0
        path = [0] * 10
        
        while p or stack:
            if p:
                path[p.val] += 1
                stack.append(p)
                p = p.left
            else:
                cur = stack[-1]
                if cur.right and cur.right != lastVisited:
                    p = cur.right
                else:
                    if not cur.left and not cur.right and self.isPseudoPalindromic(path):
                        res += 1
                    lastVisited = stack.pop()
                    path[lastVisited.val] -= 1
        return res
 
