from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        total = 0
        for key, val in cnt.items():
            if val % (key+1) == 0:
               total += (val // (key + 1)) * (key + 1)
            else:
                total += (val // (key + 1)) * (key + 1) + (key+1)
        return total



        
