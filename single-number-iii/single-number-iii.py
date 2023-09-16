class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        tmp = []
        for key in freq:
            if freq[key] == 1:
                tmp.append(key)
        return tmp