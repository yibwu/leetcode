def get_next_table(pattern):
    next = [-1, 0]
    idx = 0
    for i in range(1, len(pattern) - 1):
        if pattern[idx] == pattern[i]:
            idx += 1
            next.append(next[-1] + 1)
        else:
            if pattern[0] == pattern[i]:
                next.append(idx)
            else:
                idx = 0
                next.append(0) 
    return next


def match(s, pattern):
    if not pattern:
        return 0 
    if not s:
        return -1   

    next = get_next_table(pattern)
    i, j = 0, 0
    while i < len(s) and j < len(pattern):
        if s[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]
            if j == -1:
                i += 1
                j += 1
    return i - j if j == len(pattern) and s[i - j] == pattern[0] else -1
        
    
if __name__ == '__main__':
    cases = [
        ('acabaabaabcaccaabc', 'abaabcac'),
        ('hello', 'll'),
        ('a', 'b'),
        ('a', ''),
        ('', ''),
        ('', 'a'),
        ('aabaaabaaac', 'aabaaac'),
        ('aaaaabbbbb', 'bbbb'),
    ]
    for c in cases:
        res = match(c[0], c[1])
        print(res)
