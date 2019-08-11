def common_chars(A):
    characters = set(A[0])
    for s in A[1:]:
        characters &= set(s)
    
    res = []
    for c in characters:
        cnt = min(list(map(lambda x: x.count(c), A)))
        res.extend([c] * cnt)
    return res


if __name__ == '__main__':
    cases = [
        ["bella","label","roller"],
        ["cool","lock","cook"],
    ]
    for c in cases:
        print(common_chars(c))
