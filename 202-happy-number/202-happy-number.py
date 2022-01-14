class Solution:
    def isHappy(self, n: int) -> bool:
        # Hash set for instant look ups
        seen = set()
        while n > 0 and n not in seen:
            seen.add(n)
            n =  sum([int(x)**2 for x in str(n)])
        return n == 1 