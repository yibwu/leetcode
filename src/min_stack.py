# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.stack = []
        self.min_elem = None

    def push(self, node):
        if self.min_elem is None or node < self.min_elem:
            self.min_elem = node
        self.stack.append(node)

    def pop(self):
        node = self.stack.pop(-1)
        if node == self.min_elem:
            if self.stack:
                self.min_elem = min(self.stack)
            else:
                self.min_elem = None
        else:
            if not self.stack:
                self.min_elem = None
        return node

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_elem


if __name__ == '__main__':
    o = Solution()
    res = []
    directives = ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
    for d in directives:
        if d.startswith('PSH'):
            num = int(d.split('PSH')[-1])
            o.push(num)
        elif d.startswith('MIN'):
            res.append(o.min())
        elif d.startswith('POP'):
            o.pop()
    print(res)