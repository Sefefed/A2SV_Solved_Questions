class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = []
        result = len(temperatures) * [0]
        for i in range(len(temperatures)):
                while st and temperatures[st[-1]] < temperatures[i]:
                    indices = st.pop()
                    result[indices] = i - indices
                st.append(i) 
        return result     
