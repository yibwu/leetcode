class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s[::-1]
        result = ''
        start = 0
        in_word = False
        i = 0

        while i < len(s):
            if s[i] == ' ':
                if not in_word:
                    pass
                else:
                    in_word = False
                    result += s[start: i][::-1]
                    result += ' '
            else:
                if not in_word:
                    start = i
                    in_word = True
                else:
                    pass
            i += 1
        result += s[start:][::-1]
        return result


if __name__ == '__main__':
    o = Solution()
    s = 'a  bc   def '
    ret = o.reverseWords(s)
    print(ret)
    print(len(ret))
    
