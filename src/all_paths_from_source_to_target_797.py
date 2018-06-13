class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        degree = self.get_degree(graph)
        start_vertexes = [k for k, v in enumerate(degree) if v == 0]
        result = []
        tmp = []
        for v in start_vertexes:
            self.visited(v, tmp, result, graph)
        return result

    def get_zero_degree(self, degree):
        return [k for k, v in enumerate(degree) if v == 0]

    def visited(self, i, tmp, result, graph):
        tmp.append(i)
        if i == len(graph) - 1:
            import copy
            result.append(copy.deepcopy(tmp))
        for v in graph[i]:
            self.visited(v, tmp, result, graph)
        tmp.remove(i)

    def get_degree(self, graph):
        d = {i: 0 for i in range(len(graph))}
        for edge in graph:
            for v in edge:
                d[v] = d.get(v, 0) + 1
        return d


if __name__ == '__main__':
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    o = Solution()
    ret = o.allPathsSourceTarget(graph)
    print(ret)