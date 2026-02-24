class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, 0
        people.sort()
        while r < len(people) - 1 and people[l] + people[r+1] <= limit:
            r += 1
        boats = len(people) - 1 - r
        while l <= r and r < len(people):
            if l<r and people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            elif l < r and people[l] + people[r] > limit:
                boats += 1
                r -= 1   
            else:
                boats += 1 
                l += 1
                r -= 1 
        return boats            


        
