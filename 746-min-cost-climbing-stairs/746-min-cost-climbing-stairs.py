class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         minimumCost = [0] * (len(cost) + 1)
#         for i in range(2, len(cost)+1):
#             minimumCost[i] = min(cost[i-2]+ minimumCost[i-2], cost[i-1]+minimumCost[i-1])
        
#         return minimumCost[-1]
#Top down(memoization)
#         def minimum_cost(i):
#             if i == 0 or i == 1:
#                 return 0
#             if i in memo:
#                 return memo[i]
#             one_down = minimum_cost(i-1) + cost[i-1]
#             two_down = minimum_cost(i-2) + cost[i-2]
#             memo[i] = min(one_down, two_down)
#             return memo[i]
        
#         memo = {}
#         return minimum_cost(len(cost))
        downOne, downTwo = 0,0 
        for i in range(2, len(cost) +1):
            tmp = downOne
            downOne = min(downOne + cost[i-1], downTwo + cost[i-2])
            downTwo = tmp
        return downOne
            