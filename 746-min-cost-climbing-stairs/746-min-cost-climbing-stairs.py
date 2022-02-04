class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first_step,second_step = 0, 0
        minimumCost = [0] * (len(cost) + 1)
        for i in range(2, len(cost)+1):
            minimumCost[i] = min(cost[i-2]+ minimumCost[i-2], cost[i-1]+minimumCost[i-1])
        
        return minimumCost[-1]
                                                        