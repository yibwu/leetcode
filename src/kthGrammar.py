def kthGrammar(N, K):
    if N == 1 and K == 1:
        return 0
    elif N == 2:
        return 0 if K == 1 else 1
    else:
        import math
        if kthGrammar(N - 1, int(math.ceil(K / 2))) == 1:
            return 1 if K & 1 else 0
        else:
            return 0 if (K & 1) else 1


if __name__ == '__main__':
    cases = [
        (1, 1),
        (2, 1),
        (2, 2),
        (4, 5),
    ]
    for c in cases:
        print(kthGrammar(c[0], c[1]))
