def rob(nums):
    if not nums:
        return 0

    nums.insert(0, 0)
    i = 2
    while i < len(nums):
        nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        i += 1
    return nums[-1]


if __name__ == '__main__':
    cases = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [2, 1, 1, 2],
        [1, 3, 1],
    ]

    for c in cases:
        print(c)
        print(rob(c))
