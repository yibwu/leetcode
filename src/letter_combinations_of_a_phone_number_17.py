class Solution:
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        TABLE = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        letters = [TABLE[d] for d in digits]
        result = []
        self.helper(letters, 0, result)
        return list(filter(lambda x: len(x) == len(letters), result))

    def helper(self, letters, index, result):
        if index == len(letters) - 1:
            for ch in letters[index]:
                result.append(ch)
            return
        else:
            self.helper(letters, index + 1, result)
            result_n_1 = list(filter(lambda x: len(x) == len(letters) - index - 1, result))
            for ch in letters[index]:
                for item in result_n_1:
                    result.append(ch + item)
            return


if __name__ == '__main__':
    o = Solution()
    digits = '23'
    ret = o.letter_combinations(digits)
    print(ret)
