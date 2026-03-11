# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        st = []
        while curr:
            if st and curr.val > st[-1].val:
                while st and curr.val > st[-1].val:
                    st.pop()
                if st:
                    st[-1].next = curr
                    st.append(curr)   
                else:
                    head = curr
                    st.append(curr)
            else:
                st.append(curr) 
            curr = curr.next
        return head                   



        
