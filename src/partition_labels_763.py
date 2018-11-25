class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i, LEN = 0, len(S)
        low, partition = 0, 0
        res = []

        while i < LEN:
            cur = S[i]
            j = S.rindex(cur)
            if j > partition:
                partition = j
            if i == partition:
                res.append(S[low: partition + 1])
                low = partition + 1
            i += 1
        if low <= partition:
            res.append(S[low: partition + 1])
        return list(map(lambda x: len(x), res))


if __name__ == '__main__':
    o = Solution()
    # s = 'caba'
    # s = 'ababcbacadefegdehijhklij'
    # s = 'eaaaabaaec'
    # s = 'aebbedaddc'
    s = "vhaagbqkaq"
    ret = o.partitionLabels(s)
    print(ret)