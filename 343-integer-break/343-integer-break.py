class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * 58
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        
        max_prod = 1
        for i in range(4, n+1):
            dp[i] = max(dp[i], (3 * (i-3)), 3 * dp[i-3])
                
        
        return dp[n]
        