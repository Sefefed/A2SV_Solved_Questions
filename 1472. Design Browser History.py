class classNode:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = classNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = None
        to_visit = classNode(url)

        to_visit.prev = self.curr
        self.curr.next = to_visit

        self.curr = to_visit
    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.url    
    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.url    
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
