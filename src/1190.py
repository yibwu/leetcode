def reverse_parentheses(s):
    a_list = []
    stack = []
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            lo = stack.pop()
            a_list.append((lo, i))
            
    for tup in a_list:
        i, j = tup[0], tup[1]
        t = s[:i+1] + s[i+1: j][::-1] + s[j:]
        s = t
    s = s.replace('(', '')
    s = s.replace(')', '')
    return s


if __name__ == '__main__':
    cases = [
        '',
        'a',
        'a(b)',
        '(a(bc))',
        'a(b(cd))',
    ]
    for s in cases:
        print(reverse_parentheses(s))
