class Solution:
    
    def rob(self, nums: List[int]) -> int:
        hashmap = {}
        def dp(i:int) -> int:
            
            if i == 0:
                return nums[0]

            elif i == 1:
                return max(nums[0],nums[1])

            if i not in hashmap:
                hashmap[i] = (max(dp(i - 1), dp(i - 2) + nums[i]))
            
            return hashmap[i]
        
        
        return dp(len(nums)-1)
    
                
            
        
                
        