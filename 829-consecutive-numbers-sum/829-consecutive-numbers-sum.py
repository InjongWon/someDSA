import math
from fractions import Fraction as frac

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # lets think about sequences 
        # it has to be consecutive so 1+2+...+n-1 = n(n+1)/2 
        # in different note x + (x+1) + (x+2) + (x+3) = x + (x+1) + (x+2) + (x+n-1) where n is total number
        # imagine we are given an input n = 10
        # then 1 is already included as 10 itself. 
        # x + (x+1) + (x+2) + (x+n-1) = num_element*(first_element + last_element)/2 by the properties of arithmetic sequence
        # we know x+(x+1) + (x+2) + (x+3) = N
        # n*(x+x+n-1)/2 = n(2x+n-1)/2 = N  - properties 
        # 2xn/2 + n(n-1)/2= N
        # xn + n(n-1)/2 = N
        # xn = N - n(n-1)/2
        # since x is the starting value 1 being the inclusive value of input
        # all we need to know is that x is to be 1 so if N-n(n-1)/2 %2 == 0 means that with mod operator
        # it evenly becomes a integer factor. 
        # since x is always postivie in this case N-(n-1)/2 > 0 = N >n(n-1)/2 = 2N > n(n-1) which is roughly 
        # 2N > n(n) so 2N >n^2 = sqrt(2N) > n
        
        # initial value 
        count = 1
        # smaller values 
        n_ways = 2 
        target = math.sqrt(2*n)
        while n_ways < target:
            if (n - n_ways*(n_ways-1)/2) % n_ways == 0:
                count += 1
            n_ways += 1 
        return count
        
        # smallest size
        # count = 1 
        # s = 2
        # target = math.sqrt(2*n)
        # while s < target:
        #     if (n - s*(s-1)/2) % s == 0:
        #         count += 1
        #     s += 1
        # return count