def foo(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            pass


def init_matrix():
    matrix = [[0 for _ in range(8)] for _ in range(8)]
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
    matrix = init_matrix()
    for row in matrix:
        print(row)
