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
    bfs(graph)
