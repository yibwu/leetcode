class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        scode = 0
        for ch in s:
            scode ^= ord(ch) 

        tcode = 0
        for ch in t:
            tcode ^= ord(ch)

        return chr(scode ^ tcode) 


if __name__ == '__main__':
    o = Solution()
    s = 'abcd'
    t = 'abcde'
    ret = o.findTheDifference(s, t)   
    print(ret)
