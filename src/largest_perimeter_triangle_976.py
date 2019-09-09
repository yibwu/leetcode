def largest_perimeter(A):
    A.sort(reverse=True)

    i = 0
    while i < len(A) - 2:
        if is_valid_triangle(A[i], A[i+1], A[i+2]):
            return sum(A[i: i+3])
        else:
            i += 1
    return 0
        

# suppose a >= b >= c
def is_valid_triangle(a, b, c):
    return True if a < b + c else False


if __name__ == '__main__':
    cases = [
        [2, 1, 2],
        [1, 2, 1],
        [3, 2, 3, 4],
        [3, 6, 2, 3],
    ]
    for c in cases:
        print(largest_perimeter(c))
