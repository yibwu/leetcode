class Solution:
    def subdomain_visits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = {}

        for item in cpdomains:
            arr = item.split(' ')
            count = int(arr[0])
            domain = arr[1]
            i = domain.index('.')
            j = domain.rindex('.')
            domain_count[domain] = domain_count.get(domain, 0) + count
            domain_count[domain[i + 1:]] = domain_count.get(domain[i + 1:], 0) + count
            if i != j:
                domain_count[domain[j + 1:]] = domain_count.get(domain[j + 1:], 0) + count
            else:
                pass

        return [str(count) + ' ' + domain for domain, count in domain_count.items()]


if __name__ == '__main__':
    o = Solution()
    arr = ["9001 discuss.leetcode.com"]
    arr = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    ret = o.subdomain_visits(arr)
    print(ret)

