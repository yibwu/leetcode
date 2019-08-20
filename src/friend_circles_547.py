def find_circle_num(matrix):
    if not matrix:
        return 0

    N = len(matrix[0])
    nums = [-1 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and matrix[i][j] != 0:
                union(i, j, nums)
    cnt = 0
    for n in nums:
        if n < 0:
            cnt += 1
    return cnt
                
                
def find(x, nums):
    if nums[x] < 0:
        return x
    else:
        nums[x] = find(nums[x], nums)
        return nums[x]
    

def union(x, y, nums):
    px = find(x, nums)
    py = find(y, nums)
    if px != py:
        nums[px] += nums[py]
        nums[py] = px
    else:
        pass


if __name__ == '__main__':
    matrix = [[1, 1, 0],
              [1, 1, 0],
              [0, 0, 1]]
    print(find_circle_num(matrix))
