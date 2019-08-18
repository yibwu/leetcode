def is_perfect_square(num):
    low, high = 1, num
        
    while low <= high:
        mid = low + (high - low) // 2
        t = mid * mid
        if t > num:
            high = mid - 1
        elif t < num:
            low = mid + 1
        else:
            return True
    return False


if __name__ == '__main__':
    nums = [16, 14]
    for n in nums:
        print(is_perfect_square(n))
