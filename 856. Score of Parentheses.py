class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dep = 0
        score = 0
        for i, ch in enumerate(s):
            if ch == "(":
                dep += 1
            else:
                dep -= 1
                if s[i-1] == "(":
                    score += 2 ** dep
        return score                  

        
