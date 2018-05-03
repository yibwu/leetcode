def dfs(graph):
    vertexes = {key for key in graph}
    visited = {key: False for key in graph}

    for v in vertexes:
        if not visited[v]:
            helper(v, visited, graph)
        else:
            pass


def helper(current_vertex, visited, graph):
    print(current_vertex)
    visited[current_vertex] = True

    for neighbor in graph[current_vertex]:
        if not visited[neighbor]:
            helper(neighbor, visited, graph)
        else:
            pass


if __name__ == '__main__':
    # undirected graph represented by arrays of adjacent vertexes
    graph = {
        1: [2, 7, 8],
        2: [1, 3, 6],
        3: [2, 4, 5],
        4: [3],
        5: [3],
        6: [2],
        7: [1],
        8: [1, 9, 12],
        9: [8, 10, 11],
        10: [9],
        11: [9],
        12: [8],
    }
    dfs(graph)
