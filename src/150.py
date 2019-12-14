class Solution:

    def evalRPN(self, tokens):
        OPS = set(list('+-*/'))
        stack = []

        for t in tokens:
            if t not in OPS:
                stack.append(int(t))
            else:
                op_right = stack.pop()
                op_left = stack.pop()

                if t == '+':
                    tmp = op_left + op_right
                elif t == '-':
                    tmp = op_left - op_right
                elif t == '*':
                    tmp = op_left * op_right
                elif t == '/':
                    tmp = abs(op_left) // abs(op_right)
                    positive = (
                        op_left >= 0 and op_right > 0) or (
                        op_left <= 0 and op_right < 0)
                    tmp = tmp if positive else -tmp
                stack.append(tmp)
        return stack[0]


if __name__ == '__main__':
    cases = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    obj = Solution()
    for c in cases:
        print(obj.evalRPN(c))
