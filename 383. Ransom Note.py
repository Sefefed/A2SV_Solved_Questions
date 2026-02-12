class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        isTrue = True
        for s in ransomNote:
            if s not in magazine or ransomNote.count(s) > magazine.count(s):
                isTrue = False
        return isTrue        
        
