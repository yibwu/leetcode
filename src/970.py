def powerfulIntegers(x, y, bound):
    """
    :type x: int
    :type y: int
    :type bound: int
    :rtype: List[int]
    """
    import math
    
    lo, hi = (x, y) if x < y else (y, x)
    
    if lo != 1:
        high_bound = int(math.floor(math.log(bound, lo)))
    elif hi != 1:
        high_bound = int(math.floor(math.log(bound, hi)))
    else:
        high_bound = bound
    
    res = set([])
    for i in range(high_bound + 1):
        for j in range(high_bound + 1):
            t = math.pow(x, i) + math.pow(y, j)
            if t <= bound:
                res.add(int(t))
    return list(res)
