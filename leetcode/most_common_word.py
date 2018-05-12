# https://leetcode.com/problems/most-common-word/description/
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        for symbol in ['!', '?', "'", ",", ";", "."]:
            paragraph = paragraph.replace(symbol, '')
        words = [x for x in paragraph.split(' ') if x not in banned]

        maxCount = 0
        maxword = None

        for word in set(words):
            wcount = words.count(word)
            if wcount > maxCount:
                maxword = word
                maxCount = wcount

        return maxword
