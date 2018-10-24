class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_a = A.split(' ')
        words_b = B.split(' ')
        set_a = set(words_a)
        set_b = set(words_b)

        repeated_words_a = self.get_repeated_words(words_a)
        repeated_words_b = self.get_repeated_words(words_b)

        return list(((set_a - set_b) | (set_b - set_a)) - repeated_words_a - repeated_words_b)

    def get_repeated_words(self, words):
        word_count = dict()
        for w in words:
            count = word_count.get(w, 0)
            word_count[w] = count + 1
        repeated_words = set()
        for w, count in word_count.items():
            if count > 1:
                repeated_words.add(w)
        return repeated_words