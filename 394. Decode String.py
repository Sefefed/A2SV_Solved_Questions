class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        curr = ""
        num = ""
        for char in s:
            if char != "]":
                st.append(char)
            else:
                curr = ""
                while st and st[-1] != "[":
                    curr = st.pop() + curr
                st.pop()
                num = ""
                while st and st[-1].isdigit():
                    num = st.pop() + num
                st.append(curr * int(num))
        return "".join(st)               
        
