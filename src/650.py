def min_steps(n):
    # store [min step, max paste value]
    res = [[0, 0], [0, 0]]
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            res.append([res[i >> 1][0] + 2, i >> 1])
        else:
            j = i - 1
            min_step = 1001
            max_paste = 1
            while j >= 2:
                step, paste = res[j][0], res[j][1]
                diff = i - j
                if diff % paste == 0 and diff // paste + step < min_step:
                    min_step = diff // paste + step
                    max_paste = paste
                j -= 1
            res.append([min_step, max_paste])
    return res[n][0]


if __name__ == '__main__':
    cases = [i for i in range(1, 10)]
    for c in cases:
        print(min_steps(c))
