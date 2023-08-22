from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        
        for i in nums:
            hashMap[i] += 1
        for i in hashMap:
            if hashMap[i] == 1: 
                return i