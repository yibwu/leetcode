def can_three_parts_equal_sum(A):
    s = sum(A)
    if s % 3 != 0:
        return False
    target = s // 3
    
    i, t = 0, 0
    while i < len(A) and t != target:
        t += A[i]
        i += 1
    
    if i == 0 or i == len(A) or t != target:
        return False
    
    t = 0
    while i < len(A) and t != target:
        t += A[i]
        i += 1
        
    return True if t == target else False
