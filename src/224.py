class Solution:

    def calculate(self, s):
        s = s.replace(' ', '')
        operands = []
        operators = []
        nums = []

        for i, c in enumerate(s):
            if c.isnumeric():
                nums.append(c)
            elif nums:
                operands.append(self.get_int(nums))
                nums = []

            if i == len(s) - 1 and nums:
                operands.append(self.get_int(nums))
                nums = []

            if c == '(':
                operators.append(c)
            elif c == ')':
                self.helper(operators, operands)
                if operators and operators[-1] == '(':
                    operators.pop()
            elif c == '+' or c == '-':
                self.helper(operators, operands)
                operators.append(c)

        if nums:
            operands.append(self.get_int(nums))
        self.helper(operators, operands)
        return operands[-1]

    def get_int(self, nums):
        return int(''.join(nums))

    def helper(self, operators, operands):
        while operators and operators[-1] != '(':
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            if op == '+':
                operands.append(left + right)
            else:
                operands.append(left - right)


if __name__ == '__main__':
    cases = [
        '123456',
        '1 + 1',
        ' 2-1 + 2 ',
        '(1+(4+5+2)-3)+(6+8)',
        '(1)',
        '(1)+(2)',
    ]
    obj = Solution()
    for c in cases:
        print(obj.calculate(c))
