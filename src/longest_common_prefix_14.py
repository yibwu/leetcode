class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            result = ''
        else:
            lens = [len(s) for s in strs]
            len_min = min(lens)
            i = 0
            while i < len_min:
                prefixs = [s[:i + 1] for s in strs]
                if prefixs.count(strs[0][:i + 1]) != len(prefixs):
                    break
                else:
                    i += 1
            result = strs[0][:i]
        return result


if __name__ == '__main__':
    o = Solution()
    strs = ["flower", "flow", "flight"]
    ret = o.longest_common_prefix(strs)
    print(ret)