with open('/Users/wuyibo/result_uid.csv', 'r') as f:
    res = 0
    for line in f:
        a = line.strip().split(',')
        nums = list(map(lambda x: int(x), a))
        if nums[1] > 200:
            res += 1
            print(line)
    print(res)