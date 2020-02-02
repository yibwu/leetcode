class Trie:
    
    def __init__(self):
        self.a_dict = dict()
        self.is_word = False
        
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.a_dict:
                cur.a_dict[c] = Trie()
            cur = cur.a_dict[c]
        cur.is_word = True
        
    def prefix_count(self, word):
        cnt = 0
        cur = self
        for c in word:
            cur = cur.a_dict[c]
            if cur.is_word:
                cnt += 1
            else:
                break
        return cnt
    
    
class Solution:
    
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        max_cnt = 0
        res = ''
        for w in words:
            cnt = trie.prefix_count(w)
            if cnt > max_cnt:
                max_cnt = cnt
                res = w
            elif cnt == max_cnt and w < res:
                res = w
        return res
