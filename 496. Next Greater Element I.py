class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        dic = {}
        st = []
        for num in nums2:
            while st and num > st[-1]:
                dic[st[-1]] = num
                st.pop()
            st.append(num)   
        res = []
        for nums in nums1:
            if nums in dic:
                res.append(dic[nums])   
            else:
                res.append(-1)      
        return res        

                
