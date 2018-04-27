# https://leetcode.com/problems/top-k-frequent-words/description/

from collections import defaultdict

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        self.counts = defaultdict(int)

        for word in words:
            self.counts[word] += 1

        return sorted(set(words), key=self.keyFunc)[:k]

    def keyFunc(self, w):
        return (-self.counts[w], w)
