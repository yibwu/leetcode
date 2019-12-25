class Trie:
    
    def __init__(self):
        self.child = dict()
        self.s = ''
        
    def insert(self, s):
        cur = self
        for c in s:
            if c not in cur.child:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.s = s
        
    def match(self, s):
        cur = self
        for c in s:
            if c not in cur.child:
                return ''
            elif cur.child[c].s:
                return cur.child[c].s
            else:
                cur = cur.child[c]
        return cur.s
    
    
class Solution:
    
    def replaceWords(self, str_list, sentence):
        trie = Trie()
        for s in str_list:
            trie.insert(s)
        
        res = []
        words = sentence.split(' ')
        for w in words:
            ret = trie.match(w)
            if ret:
                res.append(ret)
            else:
                res.append(w)
        return ' '.join(res)


if __name__ == '__main__':
    a_list = ['cat', 'bat', 'rat']
    s = 'the cattle was rattled by the battery'
    obj = Solution()
    res = obj.replaceWords(a_list, s)
    print(res)
