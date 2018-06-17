class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = a.split('+')
        y = b.split('+')

        a = int(x[0]) * int(y[0])
        b = int(x[0]) * int(y[1].split('i')[0]) + int(y[0]) * int(x[1].split('i')[0])
        c = -(int(x[1].split('i')[0]) * int(y[1].split('i')[0]))

        return str(a + c) + '+' + str(b) + 'i'


if __name__ == '__main__':
    o = Solution()
    a = "1+-1i"
    b = "1+-1i"
    ret = o.complexNumberMultiply(a, b)
    print(ret)
