# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        arr = list(s)
        occur_char = False
        i = 0

        low, high = 0, 0
        while i < len(arr):
            if arr[i] != ' ':
                if not occur_char:
                    low = i
                    occur_char = True
            elif occur_char:
                high = i - 1
                self.swap_array(arr, low, high)
                occur_char = False
            i += 1
        print(low, high, occur_char)
        if occur_char:
            self.swap_array(arr, low, len(arr) - 1)
        self.swap_array(arr, 0, len(arr) - 1)
        return ''.join(arr)

    def swap_array(self, array, low, high):
        while low < high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1


if __name__ == '__main__':
    o = Solution()
    s = 'student. a am Ia'
    # s = 'I'
    # s = 'a b'
    # s = 'I am a student.'
    ret = o.ReverseSentence(s)
    print(ret)