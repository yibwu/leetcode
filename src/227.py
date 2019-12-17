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
            elif c == '*' or c == '/':
                self.helper2(operators, operands)
                operators.append(c)

        if nums:
            operands.append(self.get_int(nums))
        self.helper(operators, operands)
        return operands[-1]

    def get_int(self, nums):
        return int(''.join(nums))

    def helper2(self, operators, operands):
        while operators and operators[-1] in '*/':
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            if op == '*':
                operands.append(left * right)
            elif op == '/':
                operands.append(left // right)

    def helper(self, operators, operands):
        while operators and operators[-1] != '(':
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            if op == '+':
                operands.append(left + right)
            elif op == '-':
                operands.append(left - right)
            elif op == '*':
                operands.append(left * right)
            elif op == '/':
                operands.append(left // right)


if __name__ == '__main__':
    cases = [
        '(1*2*3)',
        '1-1+1',
        '12345',
        '(1+2)*(3+4)',
        '(1)',
        '2*3*4',
        '3+2*2',
        ' 3/2 ',
        ' 3+5 / 2 ',
        '1- 2*2 + 3*3',
    ]
    obj = Solution()
    for c in cases:
        print(c, '=>', obj.calculate(c))
