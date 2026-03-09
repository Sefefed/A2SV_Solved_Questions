class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == "*":
                if st:
                    st.pop()
            else:
                st.append(ch)        
        return "".join(st)
