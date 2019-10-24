def reverse_bits(n):
    """
    00000010100101000001111010011100
    j                              i
    """

    i, j = 0, 31
    while i < j:
        lo = 1 if n & (1 << i) else 0
        hi = 1 if n & (1 << j) else 0

        if lo == 1 and hi == 0:
            n ^= (1 << i)
            n |= (1 << j)
        elif lo == 0 and hi == 1:
            n |= (1 << i)
            n ^= (1 << j)
        i += 1
        j -= 1
    return n


if __name__ == '__main__':
    nums = [43261596, 4294967293] 
    for n in nums:
        print(reverse_bits(n))
