class RecentCounter:

    def __init__(self):
        self.que = deque()
        
    def ping(self, t: int) -> int:
        self.que.appendleft(t)
        while self.que[-1] < t-3000:
            self.que.pop()
        return len(self.que)    


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
