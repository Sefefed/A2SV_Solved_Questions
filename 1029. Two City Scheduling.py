class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_costs = 0
        costs.sort(key=lambda x:-(x[1]-x[0]))
        n = len(costs)
        for i in range(n):
            if i < n // 2:
                min_costs += costs[i][0]
            else:
                min_costs += costs[i][1] 
        return min_costs
