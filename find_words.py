from typing import List 
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = []
        lengths = 0
        count_chars = Counter(chars)
        for word in words:
            count_word = Counter(word)
            possible = True
            for char in word:
                if count_word[char] > count_chars[char]:
                    possible = False
                    break
            if possible:
                result.append(word) 
                lengths += len(word)  
        return lengths          

                      



        






        