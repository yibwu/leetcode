# -*- coding:utf-8 -*-

class Solution:
    def get_ugly_number(self, index):
        # write code here
        number = 1
        count = 0
        while count < index:
            if self.is_ugly_number(number):
                count += 1
            number += 1
        return number - 1

    def is_ugly_number(self, number):
        if number < 1:
            return False
        for i in [2, 3, 5]:
            while number != 1 and number % i == 0:
                number //= i
        return True if number == 1 else False


if __name__ == '__main__':
    o = Solution()
    ret = o.get_ugly_number(8)
    print(ret)

