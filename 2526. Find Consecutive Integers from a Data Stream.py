class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.count = k
        self.que = []
        self.cnt = 0
    def consec(self, num: int) -> bool:
        if not self.que or num == self.que[-1]:
            self.cnt += 1
            self.que.append(num)
        else:
            self.cnt = 1
            self.que.append(num)
        return True if self.val == self.que[-1] and self.cnt >= self.count else False 



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
