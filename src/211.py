class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = dict()
        self.is_word = False

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = WordDictionary()
            cur = cur.child[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.helper(word, 0, self)
        
    def helper(self, word, idx, root):
        cur = root
        for i, c in enumerate(word[idx:]):
            if c in cur.child:
                cur = cur.child[c]
            elif c != '.':
                return False
            else:
                res = []
                for _, v in cur.child.items():
                    res.append(self.helper(word, idx+i+1, v))
                return True if True in res else False
        return cur.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
