def get_connected_component(matrix):
    visited = set()
    row = len(matrix)
    col = len(matrix[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and position(i, j) not in visited:
                count += 1
                dfs(matrix, i, j, visited)
    return count


def dfs(matrix, i, j, visited):
    row = len(matrix)
    col = len(matrix[0])

    for d in range(4):
        if d == 0:    # turn right 
            if j + 1 < col and matrix[i][j + 1] == 1 and position(i, j + 1) not in visited:          
                visited.add(position(i, j + 1))
                dfs(matrix, i, j + 1, visited)
        elif d == 1:  # turn down
            if i + 1 < row and matrix[i + 1][j] == 1 and position(i + 1, j) not in visited:
                visited.add(position(i + 1, j))
                dfs(matrix, i + 1, j, visited)
        elif d == 2:  # turn left
            if j - 1 >= 0 and matrix[i][j - 1] == 1 and position(i, j - 1) not in visited:          
                visited.add(position(i, j - 1))
                dfs(matrix, i, j - 1, visited)
        else:         # turn top
            if i - 1 >= 0 and matrix[i - 1][j] == 1 and position(i - 1, j) not in visited:
                visited.add(position(i - 1, j))
                dfs(matrix, i - 1, j, visited)


def position(i, j):
    return str(i) + '_' + str(j)


def init_matrix(row, col):
    matrix = [[0 for _ in range(col)] for _ in range(row)]
    pos = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (1, 6),
        (2, 3),
        (2, 4),
        (2, 6),
        (2, 7),
        (3, 3),
        (3, 6),
        (4, 2),
        (6, 5),
        (6, 6),
        (7, 5),
    ]
    for p in pos:
        matrix[p[0]][p[1]] = 1
    return matrix


if __name__ == '__main__':
    matrix = init_matrix(8, 8)
    count = get_connected_component(matrix)
    print(count)
