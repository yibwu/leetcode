def bitwise_complement(N):
    if N == 0:
        return 1
    
    bit_width = 0
    n = N
    while n:
        bit_width += 1
        n >>= 1
    return ~N + (1 << bit_width)


if __name__ == '__main__':
    cases = [(5, 2), (7, 0), (10, 5)]
    for c in cases:
        assert bitwise_complement(c[0]) == c[1]
