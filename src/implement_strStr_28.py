def get_next(pattern):
    next = [-1, 0]
    idx = 0
    for i in range(1, len(pattern) - 1):
        if pattern[idx] == pattern[i]:
            idx += 1
            next.append(next[-1] + 1)
        else:
            if pattern[0] == pattern[i]:
                idx = 1
                next.append(1)
            else:
                idx = 0
                next.append(0)
    return next


def match(s, pattern):
    next = get_next(pattern)
    i, j = 0, 0
    while i < len(s) and j < len(pattern):
        if s[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if next[j] == -1:
                i += 1
                j += 1
            else:
                j = next[j]
    return i - j if j == len(pattern) else -1
        
    
if __name__ == '__main__':
    s = 'acabaabaabcaccaabc'
    pattern = 'abaabcac'
    res = match(s, pattern)
    print(res)
