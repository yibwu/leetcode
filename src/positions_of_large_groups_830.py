class Solution(object):
    def large_group_positions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        if len(S) >= 3:
            i, j = 0, 1
            while i < len(S) - 1:
                while j < len(S) and S[i] == S[j]:
                    j += 1
                if j - i >= 3:
                    result.append([i, j - 1])
                i = j
                j = i + 1
        return result


if __name__ == '__main__':
    o = Solution()
    s = "abbxxxxzzy"
    # s = "abcdddeeeeaabbbcd"
    ret = o.large_group_positions(s)
    print(ret)
