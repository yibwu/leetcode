class Solution(object):
    def custom_sort_string(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ''
        ch_count = {}

        for ch in T:
            if ch in S:
                ch_count[ch] = ch_count.get(ch, 0) + 1
            else:
                result += ch

        for ch in S:
            if ch in ch_count:
                result += ch * ch_count[ch]

        return result


if __name__ == '__main__':
    S = "kqep"
    T = "pekeq"
    o = Solution()
    ret = o.custom_sort_string(S, T)
    print(ret)
