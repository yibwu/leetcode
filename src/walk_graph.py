def dfs(graph):
    vertexes = {key for key in graph}
    visited = set()

    for v in vertexes:
        if v not in visited:
            helper(v, visited, graph)
        else:
            pass


def helper(current_vertex, visited, graph):
    print(current_vertex)
    visited.add(current_vertex)

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            helper(neighbor, visited, graph)
        else:
            pass


def dfs2(matrix):
    vertexes = [i for i in range(1, len(matrix) + 1)]
    visited = set()
    for i, v in enumerate(vertexes):
        if v not in visited:
            helper2(i, matrix, visited, vertexes)
        else:
            pass


def helper2(i, matrix, visited, vertexes):
    print(vertexes[i])
    visited.add(i)
    for idx, val in enumerate(matrix[i]):
        if val == 1 and idx not in visited:
            helper2(idx, matrix, visited, vertexes)
        else:
            pass


def bfs(graph):
    vertexes = [key for key in graph]
    visited = set()
    queue = []

    if vertexes:
        queue.append(vertexes[0])
        while len(queue) > 0:
            cur_vertex = queue.pop(0)
            visited.add(cur_vertex)
            print(cur_vertex)
            for neighbor in graph[cur_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                else:
                    pass
    else:
        print('graph is empty!')


def bfs2(matrix):
    vertexes = [i for i in range(1, len(matrix) + 1)]
    queue = []
    visited = set()

    if len(matrix) > 0 and len(matrix[0]) > 0:
        start_idx = 0
        queue.append(start_idx)
        visited.add(start_idx)
        while len(queue) > 0:
            cur_idx = queue.pop(0)
            print(vertexes[cur_idx])
            for i, val in enumerate(matrix[cur_idx]):
                if val == 1 and i not in visited:
                    queue.append(i)
                    visited.add(i)
                else:
                    pass
    else:
        print('matrix is empty!')


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
    # undirected graph represented by adjacency matrix
    matrix = [
        [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    ]
    dfs(graph)
    bfs(graph)
    dfs2(matrix)
    bfs2(matrix)
