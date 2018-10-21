class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        lst = list(S)
        i, j = 0, len(lst) - 1
        while i < j:
            if lst[i].isalpha():
                if lst[j].isalpha():
                    lst[i], lst[j] = lst[j], lst[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                if lst[j].isalpha():
                    i += 1
                else:
                    i += 1
                    j -= 1
        return ''.join(lst)


if __name__ == '__main__':
    o = Solution()
    s = 'ab-cd'
    s = 'a-bC-dEf-ghIj'
    s = 'Test1ng-Leet=code-Q!'
    result = o.reverseOnlyLetters(s)
    print(result)