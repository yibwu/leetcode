# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        import copy
        # nums will be treated a stack
        nums = []
        ancestor_p = []
        ancestor_q = []
        last_visited = None
        found_p, found_q = False, False

        while root is not None or len(nums) != 0:
            if root is not None:
                nums.append(root)
                root = root.left
            elif len(nums) != 0:
                tmp = nums[-1]
                if tmp.right is not None and tmp.right != last_visited:
                    root = tmp.right
                else:
                    tmp = nums.pop()
                    last_visited = tmp
                    if tmp == p:
                        ancestor_p = copy.copy(nums)
                        ancestor_p.append(tmp)
                        found_p = True
                    if tmp == q:
                        ancestor_q = copy.copy(nums)
                        ancestor_q.append(tmp)
                        found_q = True
                    if found_p and found_q:
                        break
            else:
                pass
        return self.find_LCA(ancestor_p, ancestor_q)

    def find_LCA(self, ancestor_p, ancestor_q):
        lca = None
        i = 0
        while i < len(ancestor_p) and i < len(ancestor_q) and ancestor_p[i] == ancestor_q[i]:
            lca = ancestor_p[i]
            i += 1
        return lca


if __name__ == '__main__':
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node2.left = None
    node2.right = node1

    o = Solution()
    ret = o.lowestCommonAncestor(node2, node2, node1)
    print(ret.val)
