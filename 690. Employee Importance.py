"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        for emp in employees:
            dic[emp.id] = emp.importance
        imp = 0
        que = deque()
        que.append(id)
        while que:
            cur = que.popleft()
            imp += dic[cur]
            for emply in employees:
                if emply.id == cur:
                    for num in emply.subordinates:
                        que.append(num)
        return imp    



        
