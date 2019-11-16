# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return [target.val]
        graph = self.transfer_btree_to_graph(root)
        res = self.dfs(graph, target, K)
        return res

    def transfer_btree_to_graph(self, root):
        graph = dict()
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                graph.setdefault(cur.val, []).append(cur.left.val)
                graph.setdefault(cur.left.val, []).append(cur.val)
            if cur.right:
                queue.append(cur.right)
                graph.setdefault(cur.val, []).append(cur.right.val)
                graph.setdefault(cur.right.val, []).append(cur.val)
        return graph

    def dfs(self, graph, target, K):
        visited = set([target.val])
        step = [0]
        res = []
        if target.val in graph:
            for n in graph[target.val]:
                if n not in visited:
                    self.helper(graph, visited, n, res, step, K)
                    step[0] = 0
        return res

    def helper(self, graph, visited, n, res, step, K):
        visited.add(n)
        step[0] += 1
        if step[0] == K:
            res.append(n)
            step[0] -= 1
            return
        else:
            for nn in graph[n]:
                if nn not in visited:
                    self.helper(graph, visited, nn, res, step, K)
            step[0] -= 1
