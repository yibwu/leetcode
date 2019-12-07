def trap(height):
    i, j = 0, len(height) - 1
    res = 0

    while i < j:
        while i < j and height[i] == 0:
            i += 1
        while i < j and height[j] == 0:
            j -= 1

        if i < j:
            if height[i] < height[j]:
                t = height[i]
                while i < j and height[i] <= t:
                    res += (t - height[i] if t > height[i] else 0)
                    i += 1
            else:
                t = height[j]
                while i < j and height[j] <= t:
                    res += (t - height[j] if t > height[j] else 0)
                    j -= 1
    return res


if __name__ == '__main__':
    cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [5, 2, 1, 2, 1, 5],
        [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3],
    ]
    for c in cases:
        print(trap(c))
