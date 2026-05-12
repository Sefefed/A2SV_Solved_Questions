class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        new = [(a, b, i) for i, (a, b) in enumerate(tasks)]
        new.sort()
        new = deque(new)
        st, pr, i = new.popleft()
        tm = st
        heap = [(pr, i)]
        ans = []
        while heap:
            pr, i = heappop(heap)
            ans.append(i)
            tm += tasks[i][1]
            if new and not heap and not new[0][0] <= tm:
                tm = new[0][0]
            while new and new[0][0] <= tm:
                st, pr, i = new.popleft()
                heappush(heap, (pr, i))
        return ans        




         
