class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Bottom Up(tabulation)
        
        minimum = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            minimum[i] = min(minimum[i-1]+ cost[i-1], minimum[i-2]+cost[i-2])
        return minimum[-1]
        