from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        sorted_words = sorted(count.keys(), key=lambda word:(-count[word], word))
        return sorted_words[:k] 
        
