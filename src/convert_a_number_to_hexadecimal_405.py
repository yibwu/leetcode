class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        MIN = -(1 << 31)
        BASE = 16
        TAB = '0123456789abcdef'
        result = []

        if num == MIN:
            return '10000000'
        if num == 0:
            return '0'
        is_negative = True if num < 0 else False
        if is_negative:
            num = -num
        if is_negative:
            while num != 0:
                result.insert(0, num % 2)
                num //= 2
            for _ in range(32 - len(result)):
                result.insert(0, 0)
            for i in range(32):
                if result[i] == 0:
                    result[i] = 1
                else:
                    result[i] = 0
            carry = 1
            for i in range(31, 1, -1):
                if result[i] == 1 and carry == 1:
                    result[i] = 0
                    carry = 1
                else:
                    result[i] = carry
                    break
            arr = []
            for i in range(0, 32, 4):
                tmp = 0
                for j in range(i, i + 4):
                    tmp <<= 1
                    tmp += result[j]
                arr.append(TAB[tmp])
            result = arr
        else:
            while num != 0:
                result.insert(0, TAB[num % BASE])
                num //= BASE

        return ''.join(result)


if __name__ == '__main__':
    o = Solution()
    ret = o.toHex(34)
    print(ret)