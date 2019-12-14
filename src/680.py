class Solution:

    def validPalindrome(self, s):
        i, j = 0, len(s) - 1
        possible_ans = []

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if j - i == 1:
                    return True
                if s[i + 1] == s[j]:
                    possible_ans.append([i + 1, j])
                if s[i] == s[j - 1]:
                    possible_ans.append([i, j - 1])
                if not possible_ans:
                    return False
                else:
                    break
        if i >= j:
            return True

        for p in possible_ans:
            if self.isValid(s, p[0], p[1]):
                return True
        return False

    def isValid(self, s, i, j):
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        return False if i < j else True


if __name__ == '__main__':
    cases = [
        'aba',
        'abca',
    ]
    obj = Solution()
    for s in cases:
        print(obj.validPalindrome(s))
