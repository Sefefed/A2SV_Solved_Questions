class Solution:
    def minMoves(self, target: int, max_: int) -> int:
        temp = target
        move = 0
        while target != 1 and max_ > 0:
                if target % 2 == 0:
                    move += 1
                    target //= 2
                    max_ -= 1
                else:
                    move += 1
                    target -= 1    
        if target > 1:
            move += target - 1                
        return move

