class Solution:

    def calculate(self, s):
        s = s.replace(' ', '')
        operand = []
        operator = []
        nums = []

        for i, c in enumerate(s):
            if c.isnumeric():
                nums.append(c)
            elif nums:
                operand.append(self.get_int(nums))
                nums = []

            if i == len(s) - 1 and nums:
                operand.append(self.get_int(nums))
                nums = []

            if c == '(':
                operator.append(c)
            elif c == ')':
                self.helper(operator, operand)
                if operator and operator[-1] == '(':
                    operator.pop()
            elif c == '+' or c == '-':
                self.helper(operator, operand)
                operator.append(c)
            elif c == '*' or c == '/':
                self.helper2(operator, operand)
                operator.append(c)

        if nums:
            operand.append(self.get_int(nums))
        self.helper(operator, operand)
        return operand[-1]

    def get_int(self, nums):
        return int(''.join(nums))

    def helper2(self, operator, operand):
        while operator and operator[-1] in '*/':
            op = operator.pop()
            right = operand.pop()
            left = operand.pop()
            if op == '*':
                operand.append(left * right)
            elif op == '/':
                operand.append(left // right)

    def helper(self, operator, operand):
        while operator and operator[-1] != '(':
            op = operator.pop()
            right = operand.pop()
            left = operand.pop()
            if op == '+':
                operand.append(left + right)
            elif op == '-':
                operand.append(left - right)
            elif op == '*':
                operand.append(left * right)
            elif op == '/':
                operand.append(left // right)


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
