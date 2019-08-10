def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i < j:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
    return True 
    

if __name__ == '__main__':
    cases = [
        'A man, a plan, a canal: Panama',
        'race a car',
    ]
    for c in cases:
        print(is_palindrome(c))
