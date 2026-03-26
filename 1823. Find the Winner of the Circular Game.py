class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i+1 for i in range(n)]
        def winner(ind, players):
            if len(players) == 1:
                return players[0]
            indices =  (ind+k-1) % len(players)   
            players.pop(indices)
            return winner(indices, players) 
        return winner(0, players)    

        
